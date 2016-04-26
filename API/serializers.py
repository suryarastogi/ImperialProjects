from rest_framework import serializers

from models import BlockVizRequest

class BlockVizRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockVizRequest
        fields = ('created', 'start', 'end', 'threshold', 'path', 'completed')