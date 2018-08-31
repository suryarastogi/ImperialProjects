from rest_framework import serializers

from openapi.models import GraphQuery
from openapi.models import PredictionGraph
from openapi.models import PredictionGraphPoint

from openapi.models import HeatMapLocalQuery
from openapi.models import HeatMapLocal
from openapi.models import HeatMapLocalPoint

from openapi.models import HeatMapPostcodeQuery
from openapi.models import HeatMapPostcode
from openapi.models import HeatMapPostcodePoint

from openapi.models import GridSquareData

from openapi.models import PROPERTY_CHOICES, ESTATE_CHOICES

# Serialzers for the Models, using DRF Serializers

#-------------------------------------------------------------------------------
class HeatMapPostcodePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeatMapPostcodePoint
        fields = ('postcode', 'value') 

class HeatMapPostcodeSerializer(serializers.ModelSerializer):
    points =  HeatMapPostcodePointSerializer(many=True, read_only=True)
    class Meta:
        model = HeatMapPostcode
        fields = ('id','points')

class HeatMapPostcodeQuerySerializer(serializers.ModelSerializer):    
    heat_map = HeatMapPostcodeSerializer(read_only=True)   
    class Meta:
        model = HeatMapPostcodeQuery
        fields = ('loaded', 'estate_type','property_type', 'date','heat_map')

class HeatMapLocalPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeatMapLocalPoint
        fields = ('longitude','latitude', 'value') 

class HeatMapLocalPointPlusSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeatMapLocalPoint
        fields = ('longitude','latitude', 'date','estate_type','property_type', 'value') 

class HeatMapLocalSerializer(serializers.ModelSerializer):
    points =  HeatMapLocalPointSerializer(many=True, read_only=True)
    class Meta:
        model = HeatMapLocal
        fields = ('points',)

class HeatMapLocalQuerySerializer(serializers.ModelSerializer):    
    heat_map = HeatMapLocalSerializer(read_only=True)   
    class Meta:
        model = HeatMapLocalQuery
        fields = ('loaded','longitude','latitude','estate_type','property_type', 'date', 'radius','heat_map')



#-------------------------------------------------------------------------------
class PredictionGraphPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionGraphPoint
        fields = ('point_type', 'price', 'sigma', 'time') 

class PredictionGraphSerializer(serializers.ModelSerializer):
    points = PredictionGraphPointSerializer(many=True, read_only=True)
    class Meta:
        model = PredictionGraph
        fields = ('id','points')

class GraphQuerySerializer(serializers.ModelSerializer):    
    graph = PredictionGraphSerializer(read_only=True)   
    class Meta:
        model = GraphQuery
        fields = ('id','loaded','longitude','latitude','estate_type','property_type','graph')
        
        
#-------------------------------------------------------------------------------

class GridSquareDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GridSquareData
        fields = ('id', 'longitude', 'latitude')
