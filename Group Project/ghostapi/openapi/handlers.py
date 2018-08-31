# OpenAPI Signal Handlers
# Concurrency controlled through handlers

from models import HeatMapLocalQuery, heat_map_local_signal, heat_map_postcode_signal
from models import GraphQuery, graph_signal
from django.dispatch import receiver
from tasks import generate_local_map, generate_postcode_map, generate_graph
from django.conf import settings

# Used to call tasks (prevents circular import issues)
@receiver(heat_map_local_signal)
def heat_map_local_signal_receiver(sender, **kwargs):
    if settings.ASYNCH_EXEC:
        generate_local_map.delay(kwargs['id'])
    else:
        generate_local_map(kwargs['id'])

@receiver(heat_map_postcode_signal)
def heat_map_postcode_signal_receiver(sender, **kwargs):
    if settings.ASYNCH_EXEC:
        raise Exception("Template method called")        
        #generate_postcode_map.delay(kwargs['id'])
    else:
        raise Exception("Template method called")
        #generate_postcode_map(kwargs['id'])
        
# Used to forward signal to generate graph queries
@receiver(graph_signal)
def graph_signal_receiver(sender, **kwargs):
    if settings.ASYNCH_EXEC:
        generate_graph.delay(kwargs['id'])
    else:
        generate_graph(kwargs['id'])