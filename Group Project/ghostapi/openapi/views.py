from django.views.generic import View
from django.http import HttpResponse, HttpResponseNotFound

from rest_framework import generics

from openapi.models import GraphQuery
from openapi.serializers import GraphQuerySerializer
from openapi.models import PredictionGraph
from openapi.serializers import PredictionGraphSerializer
from openapi.models import PredictionGraphPoint
from openapi.serializers import PredictionGraphPointSerializer

from openapi.models import HeatMapLocalQuery
from openapi.serializers import HeatMapLocalQuerySerializer
from openapi.models import HeatMapLocal
from openapi.serializers import HeatMapLocalSerializer
from openapi.models import HeatMapLocalPoint
from openapi.serializers import HeatMapLocalPointSerializer
from openapi.serializers import HeatMapLocalPointPlusSerializer

from openapi.models import HeatMapPostcodeQuery
from openapi.serializers import HeatMapPostcodeQuerySerializer
from openapi.models import HeatMapPostcode, heat_map_postcode_signal
from openapi.serializers import HeatMapPostcodeSerializer
from openapi.models import HeatMapPostcodePoint
from openapi.serializers import HeatMapPostcodePointSerializer

from openapi.models import GridSquareData
from openapi.serializers import GridSquareDataSerializer

from openapi.models import PROPERTY_DICT, ESTATE_DICT
from openapi.utils import Utils, KM_TO_LA, KM_TO_LO

import timeit
import numpy as np
import matplotlib.pyplot as plt
import mpld3

from openapi.models import DELTA_LO, DELTA_LA
from django.views.decorators.clickjacking import xframe_options_exempt

#-------------------------------------------------------------------------------
# Graph rendered in HTML and JS for embedding into AngularJS
# @xframe_options_exempt to allow window to be included into another
@xframe_options_exempt
def graph_render(request):
    pt = request.GET.get('property_type', "S")
    et = request.GET.get('estate_type', 'L')
    
    lo = float(request.GET.get('longitude', -0.0746))
    la = float(request.GET.get('latitude', 51.385))
    
    # Range around to which a value converges
    epsilon = .5
    #Quarter of radius away
    lo_range = epsilon*-DELTA_LO
    la_range = epsilon*-DELTA_LA

    min_lo, max_lo = Utils.max_min_value(lo, lo_range)
    min_la, max_la = Utils.max_min_value(la, la_range)
    
    query = GraphQuery.objects.filter(property_type=pt, 
                                         estate_type=et,
                                         longitude__gt=min_lo,
                                         longitude__lte=max_lo,
                                         latitude__gt=min_la,
                                         latitude__lte=max_la)
    if len(query) == 0:
        return HttpResponseNotFound('<h1>No Graph Ready to call Render (call graph search first)</h1>')
    else:
        query = query[0] #First result
    
    points = query.graph.points.all()
    tuples = [(point.time, point.price, point.sigma) for point in points]
    tuples = sorted(tuples, key=lambda x: x[0])
    
    price_preds = [tup[1] for tup in tuples]
    sigmas = [tup[2] for tup in tuples]
    dates = [tup[0] for tup in tuples]
    
    price_preds, sigmas, t = np.asarray(price_preds), np.asarray(sigmas), np.asarray(dates)
    fig = plt.figure()
    # fig.set_size_inches(18, 11)
    #fig.subplots_adjust(left=0.06, bottom=0.03, right=0.98, top=0.97)
    pred_plot, = plt.plot(t, price_preds, color='#000000', ls='-', lw=1, label="Price Prediction")

    #if(datapoints != None):
    #    d_dates, d_prices = datapoints
    #    data_plot, = plt.plot(d_dates, d_prices, 'x', ls='', label="Datapoints")

    plt.fill(np.concatenate([t, t[::-1]]),
             np.concatenate([(price_preds - 1.9600 * sigmas),
                             (price_preds + 1.9600 * sigmas)[::-1]]),
             alpha=.15, fc='#000000', ec='None', label='95% confidence interval')
    plt.title("Price vs. Time")
    plt.ylabel('Price')
    # fig.savefig('graphs/p_vs_t_' + str(aid) + fn_suffix + "_.png")
    g = mpld3.fig_to_html(fig)
    #mpld3.show()
    plt.close('all')
    return HttpResponse(g)

# View for iOS rendering (could be refactored into previous request)
@xframe_options_exempt
def graph_render_ios(request):
    pt = request.GET.get('property_type', "S")
    et = request.GET.get('estate_type', 'L')
    
    lo = float(request.GET.get('longitude', -0.0746))
    la = float(request.GET.get('latitude', 51.385))
    width = float(request.GET.get('width', 5))
    height = float(request.GET.get('height', 4))
    # Range around to which a value converges
    epsilon = .5
    #Quarter of radius away
    lo_range = epsilon*-DELTA_LO
    la_range = epsilon*-DELTA_LA

    min_lo, max_lo = Utils.max_min_value(lo, lo_range)
    min_la, max_la = Utils.max_min_value(la, la_range)
    
    query = GraphQuery.objects.filter(property_type=pt, 
                                         estate_type=et,
                                         longitude__gt=min_lo,
                                         longitude__lte=max_lo,
                                         latitude__gt=min_la,
                                         latitude__lte=max_la)
    if len(query) == 0:
        return HttpResponseNotFound('<h1>No Graph Ready to call Render (call graph search first)</h1>')
    else:
        query = query[0] #First result
    
    points = query.graph.points.all()
    tuples = [(point.time, point.price, point.sigma) for point in points]
    tuples = sorted(tuples, key=lambda x: x[0])
    
    price_preds = [tup[1] for tup in tuples]
    sigmas = [tup[2] for tup in tuples]
    dates = [tup[0] for tup in tuples]
    
    price_preds, sigmas, t = np.asarray(price_preds), np.asarray(sigmas), np.asarray(dates)
    fig = plt.figure()
    fig.set_size_inches(width, height)
    #fig.subplots_adjust(left=0.06, bottom=0.03, right=0.98, top=0.97)
    #plt.figure(figsize=(width,height))
    pred_plot, = plt.plot(t, price_preds, color='#000000', ls='-', lw=1, label="Price Prediction")

    plt.fill(np.concatenate([t, t[::-1]]),
             np.concatenate([(price_preds - 1.9600 * sigmas),
                             (price_preds + 1.9600 * sigmas)[::-1]]),
             alpha=.15, fc='#000000', ec='None', label='95% confidence interval')
    plt.title("Price vs. Time")
    plt.ylabel('Price')
    # fig.savefig('graphs/p_vs_t_' + str(aid) + fn_suffix + "_.png")
    g = mpld3.fig_to_html(fig)
    #mpld3.show()
    plt.close('all')
    return HttpResponse(g)
    
# Graph Searh queries (for kNN custom graph)
class GraphSearch(generics.ListCreateAPIView):
    queryset = GraphQuery.objects.all()
    serializer_class = GraphQuerySerializer
    def get_queryset(self):
        queryset = None
        pt = self.request.query_params.get('property_type', 'S')
        et = self.request.query_params.get('estate_type', 'L')
        
        lo = float(self.request.query_params.get('longitude', -0.0746))
        la = float(self.request.query_params.get('latitude', 51.385))

        # Range around to which a value converges
        epsilon = .5
        #Quarter of radius away
        lo_range = epsilon*-DELTA_LO
        la_range = epsilon*-DELTA_LA

        min_lo, max_lo = Utils.max_min_value(lo, lo_range)
        min_la, max_la = Utils.max_min_value(la, la_range)
        
        if  pt in PROPERTY_DICT and et in ESTATE_DICT:    
            queryset = GraphQuery.objects.filter(property_type=pt, 
                                                 estate_type=et,
                                                 longitude__gt=min_lo,
                                                 longitude__lte=max_lo,
                                                 latitude__gt=min_la,
                                                 latitude__lte=max_la)
                                                        
            # Creates query for specific heatmap if it doesnt exist
            if len(queryset) < 1:
                queryset = GraphQuery.objects.create(property_type=pt, 
                                                     estate_type=et,
                                                     longitude=lo,
                                                     latitude=la)
                                                     
                queryset = GraphQuery.objects.filter(property_type=pt, 
                                                     estate_type=et,
                                                     longitude__gt=min_lo,
                                                     longitude__lte=max_lo,
                                                     latitude__gt=min_la,
                                                     latitude__lte=max_la)
        return queryset
    
# Postcode/district Heat Map
class HeatMapPostcodeSearch(generics.ListCreateAPIView):
    serializer_class = HeatMapPostcodeQuerySerializer
    def get_queryset(self):
        queryset = None
        pt = self.request.query_params.get('property_type', 'D')
        et = self.request.query_params.get('estate_type', 'F')
        date = float(self.request.query_params.get('date', 2000.01))
        
        # Range around to which a value converges
        epsilon = .25
        #Query granularity
        date_range = epsilon*float(1)/float(12)
        min_date, max_date = Utils.max_min_value(date, date_range)
        
        if  pt in PROPERTY_DICT and et in ESTATE_DICT:    
            queryset = HeatMapPostcodeQuery.objects.filter(property_type=pt, 
                                                        estate_type=et,
                                                        date__gt=min_date,
                                                        date__lt=max_date)
                                                        
            # Creates query for specific heatmap if it doesnt exist
            if len(queryset) < 1:
                query = HeatMapPostcodeQuery.objects.create(property_type=pt, 
                                                         estate_type=et,
                                                         date=date)
                #heat_map_postcode_signal.send(sender=self.__class__, id=query.id)
                queryset = HeatMapPostcodeQuery.objects.filter(property_type=pt, 
                                                            estate_type=et,
                                                            date__gt=min_date,
                                                            date__lt=max_date)
        return queryset

# HeatMap longitude/latitude query
class HeatMapSearch(generics.ListCreateAPIView):
    serializer_class = HeatMapLocalQuerySerializer
    def get_queryset(self):
        queryset = None
        pt = self.request.query_params.get('property_type', 'D')
        et = self.request.query_params.get('estate_type', 'F')
        
        date = float(self.request.query_params.get('date', 2014))
        lo = float(self.request.query_params.get('longitude', 0.0))
        la = float(self.request.query_params.get('latitude', 51.55))
        r = float(self.request.query_params.get('radius', 1.0))

        # Range around to which a value converges
        epsilon = .25
        #Query granularity
        date_range = epsilon*float(1)/float(12)
        #Quarter of radius away
        lo_range = epsilon*r*KM_TO_LO
        la_range = epsilon*r*KM_TO_LA

        min_date, max_date = Utils.max_min_value(date, date_range)
        min_lo, max_lo = Utils.max_min_value(lo, lo_range)
        min_la, max_la = Utils.max_min_value(la, la_range)

        if  pt in PROPERTY_DICT and et in ESTATE_DICT:    
            queryset = HeatMapLocalQuery.objects.filter(property_type=pt, 
                                                        estate_type=et,
                                                        longitude__gt=min_lo,
                                                        longitude__lt=max_lo,
                                                        latitude__gt=min_la,
                                                        latitude__lt=max_la,
                                                        date__gt=min_date,
                                                        date__lt=max_date, 
                                                        radius=r)[:1]
                                                        
            # Creates query for specific heatmap if it doesnt exist
            if len(queryset) < 1:
                query = HeatMapLocalQuery.objects.create(property_type=pt, 
                                                         estate_type=et,
                                                         longitude=lo,
                                                         latitude=la,
                                                         date=date,
                                                         radius=r)
                queryset = HeatMapLocalQuery.objects.filter(property_type=pt, 
                                                        estate_type=et,
                                                        longitude__gt=min_lo,
                                                        longitude__lt=max_lo,
                                                        latitude__gt=min_la,
                                                        latitude__lt=max_la,
                                                        date__gt=min_date,
                                                        date__lt=max_date, 
                                                        radius=r)[:1]
        return queryset
        
        
#-------------------------------------------------------------------------------

# DEBUGGING VIEWS

#-------------------------------------------------------------------------------
# Util object data view

class GridSquareDataList(generics.ListCreateAPIView):
    queryset = GridSquareData.objects.all()
    serializer_class = GridSquareDataSerializer

        
#-------------------------------------------------------------------------------
# Object analysis view
class HeatMapPostcodeQueryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HeatMapPostcodeQuery.objects.all()
    serializer_class = HeatMapPostcodeQuerySerializer

class HeatMapPostcodeQueryList(generics.ListCreateAPIView):
    queryset = HeatMapPostcodeQuery.objects.all()
    serializer_class = HeatMapPostcodeQuerySerializer

class HeatMapPostcodeList(generics.ListCreateAPIView):
    queryset = HeatMapPostcode.objects.all()
    serializer_class = HeatMapPostcodeSerializer

class HeatMapPostcodePointList(generics.ListCreateAPIView):
    queryset = HeatMapPostcodePoint.objects.all()
    serializer_class = HeatMapPostcodePointSerializer


class HeatMapLocalQueryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HeatMapLocalQuery.objects.all()
    serializer_class = HeatMapLocalQuerySerializer

class HeatMapLocalQueryList(generics.ListCreateAPIView):
    queryset = HeatMapLocalQuery.objects.all()
    serializer_class = HeatMapLocalQuerySerializer

class HeatMapLocalList(generics.ListCreateAPIView):
    queryset = HeatMapLocal.objects.all()
    serializer_class = HeatMapLocalSerializer

class HeatMapLocalPointList(generics.ListCreateAPIView):
    queryset = HeatMapLocalPoint.objects.all()[:20]
    serializer_class = HeatMapLocalPointPlusSerializer
   

    
#-------------------------------------------------------------------------------
# Graph objects
class GraphQueryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GraphQuery.objects.all()
    serializer_class = GraphQuerySerializer   
    
class GraphQueryList(generics.ListCreateAPIView):
    queryset = GraphQuery.objects.all()
    serializer_class = GraphQuerySerializer

class PredictionGraphList(generics.ListCreateAPIView):
    queryset = PredictionGraph.objects.all()
    serializer_class = PredictionGraphSerializer

class PredictionGraphPointList(generics.ListCreateAPIView):
    queryset = PredictionGraphPoint.objects.all()
    serializer_class = PredictionGraphPointSerializer
