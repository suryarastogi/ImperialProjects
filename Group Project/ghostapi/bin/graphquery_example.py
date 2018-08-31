# Script demonstrating how to populate graph data

from openapi.models import GraphQuery
from openapi.models import PredictionGraph
from openapi.models import PredictionGraphPoint

query = GraphQuery.objects.create(longitude=100.00, lattitude=100.00, property_type='D',estate_type='F')
pg = PredictionGraph.objects.create(prediction_query=query)
pgp = PredictionGraphPoint.objects.create(graph=pg, price=1000000.00,time=101, point_type='R')
