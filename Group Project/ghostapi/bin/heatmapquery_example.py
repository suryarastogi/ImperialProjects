# Script demonstrating how to populate heat map data

from openapi.models import HeatMapQuery
from openapi.models import PredictionHeatMap
from openapi.models import PredictionHeatMapPoint

# query = HeatMapQuery.objects.create(type="Postcode", property_type='D',estate_type='F')
query = HeatMapQuery.objects.get(pk=1)
# hp = PredictionHeatMap.objects.create(heat_map_query=query, date="Test")
hp = query.heatmaps.get(date="Test")
hpp = PredictionHeatMapPoint.objects.create(heat_map=hp, lattitude=101,longitude=101, value=450)
