from models import BlockVizRequest, block_viz_request_signal
from tasks import generate_block_viz

from models import AddressVizRequest, address_viz_request_signal
from tasks import generate_address_viz

from django.dispatch import receiver

@receiver(address_viz_request_signal)
def address_viz_request_signal_receiver(sender, **kwargs):
	generate_address_viz.delay(kwargs['id'])

@receiver(block_viz_request_signal)
def block_viz_request_signal_receiver(sender, **kwargs):
	#Asynch execution
	generate_block_viz.delay(kwargs['id'])