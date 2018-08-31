import random

from django.test import TestCase

from openapi.models import HeatMapLocalPoint,HeatMapLocalQuery, HeatMapLocal
from openapi.models import GraphQuery, PredictionGraph, PredictionGraphPoint

from openapi.models import GridSquareData, DELTA_LO, DELTA_LA
from openapi.seed_utils import SeedUtils

import json
import requests

# Model Tests --------------------------------------------------

class TestGraphQuery(TestCase):
    def setUp(self):
        self.squares = SeedDB.generateGridSquares()
        self.points = SeedDB.generateLocalPoints()
        self.query = SeedDB.generateGraphQuery()

    def test_field_types(self):
        query = self.query
        self.assertEqual(type(query.longitude), float)
        self.assertEqual(type(query.latitude), float)
        self.assertEqual(type(query.property_type), str)
        self.assertEqual(type(query.estate_type), str)

    def test_query_generation(self):
        graph = self.query.graph
        self.assertIsNotNone(graph)

    def test_query_points(self):
        graph = self.query.graph
        points = graph.points
        self.assertIsNotNone(points)
        self.assertIsNot(points.count(), 0)

    def test_query_point_types(self):
        graph = self.query.graph
        points = graph.points
        point = points.all()[0]
        self.assertEqual(type(point.price), float)
        self.assertEqual(type(point.sigma), float)
        self.assertEqual(type(point.time), float)
        self.assertEqual(type(point.point_type), unicode)


class TestLocalQuery(TestCase):
    def setUp(self):
        self.squares = SeedDB.generateGridSquares()
        self.points = SeedDB.generateLocalPoints()
        self.query = SeedDB.generateLocalQuery()
        

    def test_field_types(self):
        query = self.query
        self.assertEqual(type(query.longitude), float)
        self.assertEqual(type(query.latitude), float)
        self.assertEqual(type(query.property_type), str)
        self.assertEqual(type(query.estate_type), str)
        self.assertEqual(type(query.date), float)
        self.assertEqual(type(query.radius), float)

    def test_query_generation(self):
        map = self.query.heat_map
        self.assertIsNotNone(map)
    
    def test_map_population(self):
        map = self.query.heat_map
        points = map.points
        self.assertIsNotNone(points)
        self.assertIsNot(points.count(), 0)

class TestLocalPoint(TestCase):
    def setUp(self):
        self.squares = SeedDB.generateGridSquares()
        self.points = SeedDB.generateLocalPoints()

    def test_field_types(self):
        point = self.points[0]
        self.assertEqual(type(point.longitude), float)
        self.assertEqual(type(point.latitude), float)
        self.assertEqual(type(point.property_type), unicode)
        self.assertEqual(type(point.estate_type), unicode)
        self.assertEqual(type(point.date), float)
        self.assertEqual(type(point.value), float)
        self.assertEqual(type(point.sigma), float)

class TestGridSquareData(TestCase):
    def setUp(self):
        self.squares = SeedDB.generateGridSquares()

    def test_field_types(self):
        square = self.squares[0]
        self.assertEqual(type(square.longitude), float)
        self.assertEqual(type(square.latitude), float)

#Test Seed --------------------------------------------------------
class SeedDB(object):
    @staticmethod
    def generateGraphQuery():
        return GraphQuery.objects.create(property_type='F', 
                                         estate_type='F',
                                         longitude=0.0,
                                         latitude=0.0)

    @staticmethod
    def generateLocalQuery():
        return HeatMapLocalQuery.objects.create(property_type='F', 
                                                estate_type='F',
                                                longitude=0.0,
                                                latitude=0.0,
                                                date=2015.0,
                                                radius=1.0)
    @staticmethod
    def generateLocalPoints():
        for square in GridSquareData.objects.all():
            HeatMapLocalPoint.objects.create(longitude=square.longitude,
                                             latitude=square.latitude,
                                             property_type='F',
                                             estate_type='F', 
                                             date=2015.0, 
                                             sigma=random.uniform(1000000,3000000),
                                             value=random.uniform(10000000,15000000))
            
            HeatMapLocalPoint.objects.create(longitude=square.longitude,
                                             latitude=square.latitude,
                                             property_type='F',
                                             estate_type='F', 
                                             date=2015.5, 
                                             sigma=random.uniform(1000000,3000000),
                                             value=random.uniform(10000000,15000000))

            HeatMapLocalPoint.objects.create(longitude=square.longitude,
                                             latitude=square.latitude,
                                             property_type='F',
                                             estate_type='F', 
                                             date=2015.25, 
                                             sigma=random.uniform(1000000,3000000),
                                             value=random.uniform(10000000,15000000))

            HeatMapLocalPoint.objects.create(longitude=square.longitude,
                                             latitude=square.latitude,
                                             property_type='F',
                                             estate_type='F', 
                                             date=2015.75, 
                                             sigma=random.uniform(1000000,3000000),
                                             value=random.uniform(10000000,15000000))
        return HeatMapLocalPoint.objects.all()

    @staticmethod
    def generateGridSquares():
        for square in range(0,11):
            lo = square*DELTA_LO
            la = square*DELTA_LA
            GridSquareData.objects.create(longitude=lo, latitude=la)
        return GridSquareData.objects.all()