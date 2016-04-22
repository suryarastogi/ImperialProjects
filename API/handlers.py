from models import BlockVizRequest, block_viz_request_signal
from django.dispatch import receiver
from tasks import generate_block_viz

@receiver(block_viz_request_signal)
def block_viz_request_signal_receiver(sender, **kwargs):
	#Asynch execution
	generate_block_viz.delay(kwargs['id'])