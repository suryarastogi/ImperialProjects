# Seeding fuctions
# Tools used to seed/destroy the database 
from openapi.models import HeatMapLocalQuery
from openapi.models import HeatMapLocal
from openapi.models import HeatMapLocalPoint
from openapi.models import GridSquareData
from openapi.models import GridSquareCSVModel

from openapi.models import HeatMapPostcodeQuery
from openapi.models import HeatMapPostcode
from openapi.models import HeatMapPostcodePoint, POSTCODE_PREFIXES

from openapi.models import GraphQuery
from openapi.models import PredictionGraph
from openapi.models import PredictionGraphPoint


from tasks import generate_local_points, generate_postcode_shells, generate_postcode_points

from openapi.models import PROPERTY_DICT, ESTATE_DICT

from celery.task.control import discard_all

from django.conf import settings
import os

class SeedUtils(object):
    
    # Clear Celery queue
    @staticmethod
    def clear_celery():
        discard_all()
    
    # Clear calculated queries (not underlying data)
    @staticmethod
    def clear_derived():
        SeedUtils.clear_graph_db()
        HeatMapLocal.objects.all().delete()
        HeatMapLocalQuery.objects.all().delete()
        
    
    # Erase postcode entries
    @staticmethod
    def clear_postcode_db():
        HeatMapPostcodePoint.objects.all().delete()
        HeatMapPostcode.objects.all().delete()
        HeatMapPostcodeQuery.objects.all().delete()
        
    # Erase local entries (geolocation)
    @staticmethod
    def clear_local_db():
        GridSquareData.objects.all().delete()
        HeatMapLocalPoint.objects.all().delete()
        HeatMapLocal.objects.all().delete()
        HeatMapLocalQuery.objects.all().delete()
    
    # Erase graph entries
    @staticmethod
    def clear_graph_db():
        PredictionGraphPoint.objects.all().delete()
        PredictionGraph.objects.all().delete()
        GraphQuery.objects.all().delete()
    
    # Erase all entries in db
    @staticmethod
    def clear_db():
        SeedUtils.clear_postcode_db()
        SeedUtils.clear_local_db()
        SeedUtils.clear_graph_db()
        

    # Generates shells for the stored postcode queries
    # Must be run before seed_postcode_points()
    @staticmethod
    def seed_postcode_shells():
        futures = []
        for pt in PROPERTY_DICT:
            for et in ESTATE_DICT:
                futures.append(generate_postcode_shells.delay(pt, et))
        return futures


    # Queues up task to generate all the prediction points
    @staticmethod
    def seed_postcode_points():
        futures = []
        for prefix in POSTCODE_PREFIXES:
            for pt in PROPERTY_DICT:
                for et in ESTATE_DICT:
                    futures.append(generate_postcode_points.delay(prefix, pt, et))
        for query in HeatMapPostcodeQuery.objects.all():
            query.loaded = True
            query.save
        return futures
    
    @staticmethod
    def seed_specific_postcodes():
        postcodes = ['EC3V', 'TW4', 'W1Y', 'WC2A', 'IG8', 'HA2', 'EN3', 'EC2R', 'EC2V',  'W1C', 'EC4N', 'EC3M', 'EN5', 'TW10', 'IG1', 'EN4', 'HA5' ]
        futures = []
        for prefix in postcodes:
            for pt in PROPERTY_DICT:
                for et in ESTATE_DICT:
                    futures.append(generate_postcode_points.delay(prefix, pt, et))
        for query in HeatMapPostcodeQuery.objects.all():
            query.loaded = True
            query.save
        return futures


    # Seed GridSquareData
    # Must be run before seed_local_points()
    @staticmethod
    def seed_grid_square():
        path = os.path.join(settings.BASE_DIR, "data/grid_squares_db.csv")
        list = GridSquareCSVModel.import_data(data = open(path))

    # Queues up task to generate all the prediction points
    @staticmethod
    def seed_local_points():
        futures = []
        for grid_square in GridSquareData.objects.all():
            id = grid_square.id  
            for pt in PROPERTY_DICT:
                for et in ESTATE_DICT:
                    futures.append(generate_local_points.delay(id, pt, et))
        return futures
    
    # Seed all values into db
    @staticmethod
    def seed_all():
        futures = SeedUtils.seed_postcode_shells()
        SeedUtils.seed_grid_square()
        futures = futures + SeedUtils.seed_postcode_points()
        futures = futures + SeedUtils.seed_local_points()
        return futures

    

