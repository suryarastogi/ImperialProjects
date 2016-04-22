from __future__ import unicode_literals
from django.dispatch import Signal
from django.db import models


block_viz_request_signal = Signal(providing_args=['id'])

class BlockVizRequest(models.Model):
	# When the query was made
    created = models.DateTimeField(auto_now_add=True)
    # The start block for the visualisation analysis
    start = models.IntegerField()
    # The end block 
    end = models.IntegerField()
    # Connectivity threshold for subcomponents
    threshold = models.IntegerField(default=0)

    #transactions = models.TextField()
    # Path where the model is saved
    path = models.TextField(null=True)
    # Rendered/laid out
    rendered = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(BlockVizRequest, self).save(*args, **kwargs) 
        block_viz_request_signal.send(sender=self.__class__, id=self.id)

class Subcomponent(models.Model):
 	request = models.ForeignKey(BlockVizRequest, related_name="subcomponents")
 	transactions = models.TextField()
