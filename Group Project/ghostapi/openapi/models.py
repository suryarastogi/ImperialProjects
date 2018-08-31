from django.db import models
from csvImporter.model import CsvDbModel, CsvModel
from django.dispatch import Signal

# The postcode buroughs used
POSTCODE_PREFIXES = [  'E14', 'SW19', 'SW11', 'SW18', 'E17', 'SW6', 'SW16', 'SW17', 'N1',
                       'SW15', 'SE1', 'NW6', 'W2', 'NW3', 'E4', 'W4', 'SE18', 'NW10', 'E6',
                       'W5', 'SE9', 'NW2', 'SW2', 'SE16', 'E11', 'W14', 'SW4', 'W9', 'E1',
                       'SW12', 'SE6', 'SE13', 'NW1', 'W3', 'E3', 'NW9', 'N16', 'N8', 'N4',
                       'SE25', 'SE15', 'SW3', 'N9', 'NW8', 'SE3', 'SW20', 'E16', 'SE23',
                       'SE22', 'W6', 'N7', 'N17', 'W13', 'W12', 'N22', 'SW8', 'SE10', 'E2',
                       'SE19', 'E15', 'SW7', 'SE5', 'E10', 'E7', 'SE26', 'W8', 'W11',
                       'SE28', 'N10', 'NW4', 'N11', 'SW9', 'N13', 'NW11', 'SW10', 'N12',
                       'E5', 'W7', 'N14', 'N21', 'E8', 'SE12', 'N5', 'SE4', 'E13', 'N15',
                       'NW7', 'SW1V', 'N3', 'N6', 'N19', 'SE20', 'N2', 'SW14', 'E18',
                       'SW5', 'E1W', 'E12', 'SW13', 'N18', 'E9', 'SE27', 'SE8', 'NW5',
                       'SE24', 'SE14', 'W10', 'N20', 'SW1P', 'SE2', 'SE21', 'SE7', 'SE11',
                       'SW1X', 'SE17', 'EC1V', 'W1H', 'SW1W', 'EC2Y', 'W1U', 'WC1H',
                       'EC1R', 'W1K', 'W1W', 'W1G', 'W1T', 'WC1X', 'EC1M', 'WC1N', 'EC1Y',
                       'W1J', 'EC1A', 'EC2A', 'WC2H', 'EC1N', 'SW1H', 'EC4V', 'WC2B',
                       'WC2N', 'SW1E', 'WC1B', 'W1F', 'EC4A', 'WC1E', 'SW1Y', 'WC2E',
                       'W1B', 'W1D', 'SW1A', 'EC3N', 'WC1R', 'WC1A', 'EC4Y', 'W1S', 'WC2R',
                       'EC3R', 'EC4R', 'EC4M', 'WC1V', 'EC2M', 'N1C', 'EC3A', 'W1N', 'W1P',
                       'EC3V', 'TW4', 'W1Y', 'W1M', 'WC2A', 'IG8', 'HA2', 'EN3', 'EC2R',
                       'W1X', 'EC2V', 'W1V', 'W1R', 'W1C', 'EC4N', 'EC3M', 'EN5', 'TW10',
                       'IG1', 'EN4', 'HA5'  ]

# Different choice parameters       
PROPERTY_CHOICES = [('D', "Detached"),('S', "Semi-Detached"),('T',"Terraced"),('F',"Flat")]
PROPERTY_DICT = dict(PROPERTY_CHOICES)
ESTATE_CHOICES = [('F',"Freehold"),('L',"Lease")]
ESTATE_DICT = dict(ESTATE_CHOICES)

# Distance used between points in geo values
DELTA_LO = -0.00464
DELTA_LA = -0.00288

# HeatMap signal
heat_map_local_signal = Signal(providing_args=['id'])
heat_map_postcode_signal = Signal(providing_args=['id'])
# Graph signal
graph_signal = Signal(providing_args=['id'])

#-------------------------------------------------------------------------------
# Heat map global queries, using postcodes
class HeatMapPostcodeQuery(models.Model):
    # Loaded
    loaded = models.BooleanField(default=False)
    # GP params
    # Property Type (Detached, Semi-Detached, Terraced, Flat)
    property_type = models.CharField(choices=PROPERTY_CHOICES, max_length=1, blank=False)
    # Estate Type (Freehold, Lease)
    estate_type = models.CharField(choices=ESTATE_CHOICES, max_length=1, blank=False)
    
    # Search params
    # Prediction date
    date = models.FloatField()
    
    def save(self, *args, **kwargs):
        super(HeatMapPostcodeQuery, self).save(*args, **kwargs) 
        # moved to view.py
        # heat_map_postcode_signal.send(sender=self.__class__, id=self.id)

class HeatMapPostcode(models.Model):
    # Query that generated the Heat Map
    heat_map_query = models.OneToOneField(HeatMapPostcodeQuery, related_name="heat_map")

class HeatMapPostcodePoint(models.Model):
    # Geolocation
    postcode = models.CharField(max_length=10)
    # Value of the point
    value = models.FloatField()
    
    # Related to the heat map
    heat_map = models.ForeignKey(HeatMapPostcode, related_name="points")


# Heat Map local queries, for geolocations
class HeatMapLocalPoint(models.Model):
    # Geolocation
    longitude = models.FloatField()
    latitude = models.FloatField()
    
    # GP params
    # Property Type (Detached, Semi-Detached, Terraced, Flat)
    property_type = models.CharField(choices=PROPERTY_CHOICES, max_length=1, blank=False)
    # Estate Type (Freehold, Lease)
    estate_type = models.CharField(choices=ESTATE_CHOICES, max_length=1, blank=False)
    # Prediction date
    date = models.FloatField()
    
    # Value of the point
    value = models.FloatField()
    sigma = models.FloatField()

class HeatMapLocalQuery(models.Model):
    # Loaded
    loaded = models.BooleanField(default=False)
    # GP params
    # Property Type (Detached, Semi-Detached, Terraced, Flat)
    property_type = models.CharField(choices=PROPERTY_CHOICES, max_length=1, blank=False)
    # Estate Type (Freehold, Lease)
    estate_type = models.CharField(choices=ESTATE_CHOICES, max_length=1, blank=False)
    
    # Search params
    # Prediction date
    date = models.FloatField()
    # Geolocation parameters
    longitude = models.FloatField()
    latitude = models.FloatField()
    # Radius to search around
    radius = models.FloatField(default=1.0)
    
    def save(self, *args, **kwargs):
        super(HeatMapLocalQuery, self).save(*args, **kwargs) 
        heat_map_local_signal.send(sender=self.__class__, id=self.id)
           
class HeatMapLocal(models.Model):
    # Query that generated the Heat Map
    heat_map_query = models.OneToOneField(HeatMapLocalQuery, related_name="heat_map")
    # Relevant points
    points = models.ManyToManyField(HeatMapLocalPoint)


#------------------------------------------------------------------------------ 
# Prediction Graph Query - Land Registry      
class GraphQuery(models.Model):
    # If the query result has loaded
    loaded = models.BooleanField(default=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # GP params
    # Property Type (Detached, Semi-Detached, Terraced, Flat)
    property_type = models.CharField(choices=PROPERTY_CHOICES, max_length=1, blank=False)
    # Estate Type (Freehold, Lease)
    estate_type = models.CharField(choices=ESTATE_CHOICES, max_length=1, blank=False)
    
    def save(self, *args, **kwargs):
        super(GraphQuery, self).save(*args, **kwargs)
        #Graph generation
        graph_signal.send(sender=self.__class__, id=self.id)
    

# Prediction Graph generated for a query    
class PredictionGraph(models.Model):
    # Generated graph for query
    graph_query = models.OneToOneField(GraphQuery, related_name="graph")

# Points for the prediction graphs
class PredictionGraphPoint(models.Model):
    # Price value for point
    price = models.FloatField()
    # Sigmas
    sigma = models.FloatField()
    # Point in time 
    time = models.FloatField()
    # Point type, P, S, p= prediction, s=sigma
    point_type = models.CharField(max_length=1, blank=False)
    # Graph for the relevant point
    graph = models.ForeignKey(PredictionGraph, related_name="points")
    
    
    
    
#-------------------------------------------------------------------------------
# Extra Data Models 

# Grid square parameters for GP models
class GridSquareData(models.Model):
    id = models.IntegerField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

# Model to import GridSquareData using a CSV importer
class GridSquareCSVModel(CsvModel):
    from csvImporter.fields import IgnoredField, IntegerField, FloatField, CharField
    id = IntegerField()
    dataset = IgnoredField()
    dup_id = IgnoredField()
    latitude = FloatField()
    longitude = FloatField()
    size = IgnoredField()
    n = IgnoredField()
    final_kernal = IgnoredField()
    mpll = IgnoredField()
    rmse = IgnoredField()
    n_restarts_optimiser = IgnoredField()
    rbf_ls_init = IgnoredField()
    rbf_ls_lb = IgnoredField()
    rbf_ls_ub = IgnoredField()
    rq_a_init = IgnoredField()
    rq_a_lb = IgnoredField()
    rq_a_ub = IgnoredField()
    rq_ls_init = IgnoredField()
    rq_ls_lb = IgnoredField()
    rq_ls_ub = IgnoredField()
    wk_var_mult_lb = IgnoredField()
    wk_var_mult_ub = IgnoredField()
    alpha_var_multiplier = IgnoredField()
    logadj = IgnoredField()
    
    class Meta:
        delimiter = ","
        dbModel = GridSquareData
