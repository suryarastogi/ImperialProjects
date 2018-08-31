import random
import os
from django.db import OperationalError

from ghostapi.celery import app

from django.conf import settings

from openapi.models import HeatMapLocalQuery
from openapi.models import HeatMapLocal
from openapi.models import HeatMapLocalPoint

from openapi.models import HeatMapPostcodeQuery
from openapi.models import HeatMapPostcode
from openapi.models import HeatMapPostcodePoint
from openapi.models import POSTCODE_PREFIXES 

from openapi.models import GraphQuery
from openapi.models import PredictionGraph
from openapi.models import PredictionGraphPoint
from openapi.models import DELTA_LO, DELTA_LA

from openapi.models import GridSquareData

from openapi.utils import Utils, KM_TO_LA, KM_TO_LO

import math

import json


# Asynchronous tasks/jobs to be completed/queued


# Memory loading for the worker machines
# http://stackoverflow.com/questions/20819894/how-to-load-objects-in-memory-and-share-across-different-executions-of-celery-wo

min_year = 1995
max_year = 2019
granularity = float(1)/float(12)
steps = (max_year-min_year)*12 + 1
dates = [(min_year + x * granularity) for x in range(0, steps)]
# path = os.path.join(settings.BASE_DIR, "data/" + str(area)+ ".json")
#file_dir = settings.BASE_DIR + "/data/landreg/"
file_dir ="/vol/project/2015/362/g1536201/aew13/GPHandler/predsaves_backup/landreg/"

@app.task(bind=True)
def generate_graph(self, id):
    self.max_retries = None #Keep retrying
    try:
        query = GraphQuery.objects.get(pk=id)
        if not query.loaded:
            graph = PredictionGraph.objects.create(graph_query=query)
        
            radius = .4
        
            lo = query.longitude
            min_lo, max_lo = Utils.max_min_value(lo, radius*KM_TO_LO)
        
            la = query.latitude
            min_la, max_la = Utils.max_min_value(la, radius*KM_TO_LA)
        

            nn = HeatMapLocalPoint.objects.filter(property_type = query.property_type,
                                                  estate_type = query.estate_type,
                                                  longitude__gte = min_lo,
                                                  longitude__lte = max_lo,
                                                  latitude__gte = min_la,
                                                  latitude__lte = max_la,
                                                  date__gte=min_year,
                                                  date__lte=max_year)
        
            st = str(query.property_type) + ", " + str(query.estate_type) + ", " + str(min_lo) + ", " + str(max_lo) + ", " + str(min_la) + ", " + str(max_la)
            distance = {}
            value = {}
            sigma = {}
        
            for n in nn:
                d_lo = float((query.longitude - n.longitude))/float(KM_TO_LO)
                d_la = float((query.latitude - n.latitude))/float(KM_TO_LA)
                dis = float(math.sqrt(d_lo ** 2 + d_la ** 2))
            
                if(n.date not in distance):
                    distance[n.date] = 0
                    value[n.date] = 0
                    sigma[n.date] = 0
                
                distance[n.date] = distance[n.date] + dis
                value[n.date] = value[n.date] + dis*n.value
                sigma[n.date] = sigma[n.date] + dis*n.sigma
                        
            for date in distance:
                if distance[date] > 0:
                    p = float(value[date])/float(distance[date])
                    s = float(sigma[date])/float(distance[date])
                else: #Exact point/ 1 nearest neighbour
                    p = float(value[date])
                    s = float(sigma[date])
                pgp = PredictionGraphPoint.objects.create(graph=graph, price=p, sigma=s,time=date, point_type='P')
        
            graph.save()
            query.loaded = True
            query.save()
        return id
    except OperationalError as exc:
      raise self.retry(exc=exc)
     
    
        
@app.task(bind=True)
def generate_local_map(self, id):
    self.max_retries = None #Keep retrying
    try:
        query = HeatMapLocalQuery.objects.get(pk=id)
        if not query.loaded:
            heat_map = HeatMapLocal.objects.create(heat_map_query=query)
            radius = query.radius
        
            lo = query.longitude
            min_lo, max_lo = Utils.max_min_value(lo, radius*KM_TO_LO)
        
            la = query.latitude
            min_la, max_la = Utils.max_min_value(la, radius*KM_TO_LA)
        
            # Range around to which a value converges
            epsilon = .25
            date_range = epsilon*float(1)/float(12)
            min_date, max_date = Utils.max_min_value(query.date, date_range)
        
            points = HeatMapLocalPoint.objects.filter(property_type = query.property_type,
                                                      estate_type = query.estate_type,
                                                      date__gt=min_date,
                                                      date__lt=max_date, 
                                                      longitude__gt = min_lo,
                                                      longitude__lt = max_lo,
                                                      latitude__gt = min_la,
                                                      latitude__lt = max_la)
            for point in points:
                heat_map.points.add(point)
            
            heat_map.save()
        
            query.loaded = True
            query.save()
        return id
    except OperationalError as exc:
      raise self.retry(exc=exc)

@app.task
def generate_postcode_map(id):
    query = HeatMapPostcodeQuery.objects.get(pk=id)
    if not query.loaded:
        heat_map = HeatMapPostcode.objects.create(heat_map_query=query)
        
        for prefix in POSTCODE_PREFIXES:
            point = HeatMapPostcodePoint.objects.create(heat_map=heat_map,
                                                        postcode=prefix, 
                                                        value=random.uniform(1000000,10000000))
        
        query.loaded = True
        query.save()
    return id

# Generates outer shells for the pregenerated/stored postcode queries
@app.task
def generate_postcode_shells(property_type, estate_type):
  for i, date in enumerate(dates):
    query = HeatMapPostcodeQuery.objects.create(property_type=property_type, 
                                                estate_type=estate_type,
                                                date=date)
    #Query is not loaded
    heat_map = HeatMapPostcode.objects.create(heat_map_query=query)

# Generate points (gets predictions from the gps)
@app.task(bind=True)
def generate_postcode_points(self, area, property_type, estate_type):  
  self.max_retries = None #Keep retrying
  try:
    path = file_dir + str(area)+ ".json"
    with open(path) as data_file:
        data = json.load(data_file)
    price_preds = data[property_type][estate_type]['price_preds']
    sigmas = data[property_type][estate_type]['sigmas']

    for i, value in enumerate(price_preds):
      query = HeatMapPostcodeQuery.objects.get(property_type=property_type, 
                                               estate_type=estate_type,
                                               date=dates[i])
      heat_map = query.heat_map
      point = HeatMapPostcodePoint.objects.create(heat_map=heat_map,
                                                  postcode=area, 
                                                  value=value)
    return (area, property_type, estate_type)
  except OperationalError as exc:
    raise self.retry(exc=exc)
    
  



# Used To Populate initial database (gets predictions from the GP)
# Should be rerun each month for new
@app.task(bind=True)
def generate_local_points(self, area_id, property_type, estate_type):
    self.max_retries = None #Keep retrying
    try:
      grid_square = GridSquareData.objects.get(pk=area_id)
      path = file_dir + str(area_id)+ ".json"
      #path = os.path.join(settings.BASE_DIR, "data/" + str(area_id)+ ".json")
      with open(path) as data_file:
          data = json.load(data_file)
      price_preds = data[property_type][estate_type]['price_preds']
      sigmas = data[property_type][estate_type]['sigmas']

      for i, value in enumerate(price_preds):
          HeatMapLocalPoint.objects.create(longitude=grid_square.longitude,
                                           latitude=grid_square.latitude,
                                           property_type=property_type,
                                           estate_type=estate_type, 
                                           date=dates[i], 
                                           sigma=sigmas[i],
                                           value=value)
      return(area_id, property_type, estate_type)
    except OperationalError as exc:
      raise self.retry(exc=exc)
        