from rest_framework import serializers

from models import BlockVizRequest
from models import Subcomponent



class SubcomponentSerializer(serializers.ModelSerializer):
    path = serializers.CharField(read_only=True)
    class Meta:
        model = Subcomponent
        fields = ('id','created', 'path', 'txs', 'txs_length')

class SubcomponentEmbedSerializer(serializers.ModelSerializer):
    path = serializers.CharField(read_only=True)
    class Meta:
        model = Subcomponent
        fields = ('id','created', 'path')

class BlockVizRequestSerializer(serializers.ModelSerializer):
    path = serializers.CharField(read_only=True)
    #completed = serializers.BooleanField(read_only=True)

    subcomponents = SubcomponentEmbedSerializer(many=True, read_only=True)
    class Meta:
        model = BlockVizRequest
        fields = ('id', 'created', 'start', 'end', 'threshold', 'path', 'completed', 'subcomponents')

class BlockVizSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockVizRequest
        fields = ('id','created', 'path', 'completed')
