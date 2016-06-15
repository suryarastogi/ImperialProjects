from __future__ import unicode_literals
from django.dispatch import Signal
from django.db import models


block_viz_request_signal = Signal(providing_args=['id'])
address_viz_request_signal = Signal(providing_args=['id'])
trace_tx_viz_request_signal = Signal(providing_args=['id'])

class TraceTxVizRequest(models.Model):
    # When the query was made
    created = models.DateTimeField(auto_now_add=True)
    # Desired Transaction
    hash_index = models.TextField()

    # Path where the model is saved
    path = models.TextField(null=True)
    # Layout generation completed
    completed = models.BooleanField(default=False)
    # Comment About The Resulting Request
    comment = models.TextField(null=True)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(TraceTxVizRequest, self).save(*args, **kwargs) 
        if not self.completed:
            trace_tx_viz_request_signal.send(sender=self.__class__, id=self.id)

class AddressVizRequest(models.Model):
    # When the query was made
    created = models.DateTimeField(auto_now_add=True)
    # Desired address
    address = models.TextField()
    # Offset to pull data from
    tx_offset = models.IntegerField(default=0)
    # Amount of transactions
    tx_limit = models.IntegerField(default=50)

    # Path where the model is saved
    path = models.TextField(null=True)
    # Layout generation completed
    completed = models.BooleanField(default=False)
    # Comment About The Resulting Request
    comment = models.TextField(null=True)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(AddressVizRequest, self).save(*args, **kwargs) 
        if not self.completed:
            address_viz_request_signal.send(sender=self.__class__, id=self.id)

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
    # Layout generation completed
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(BlockVizRequest, self).save(*args, **kwargs) 
        if not self.completed:
            block_viz_request_signal.send(sender=self.__class__, id=self.id)

class Subcomponent(models.Model):
    # When the subcomponent was created
    created = models.DateTimeField(auto_now_add=True)
    # The request related to the component
    request = models.ForeignKey(BlockVizRequest, related_name="subcomponents")
    # String with list of tx indexes
    txs = models.TextField(null=True)
    
    txs_length = models.IntegerField(null=True)
    path = models.TextField(null=True)

