from rest_framework import serializers

from models import BlockVizRequest, Subcomponent
from models import AddressVizRequest
from models import TraceTxVizRequest

from graphing import EdgeData

class EdgeDataSerializer(serializers.Serializer):
    start = serializers.CharField()
    end = serializers.CharField()
    edge_type = serializers.CharField()

    def create(self, validated_data):
        return EdgeData(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance

class TraceTxVizRequestSerializer(serializers.ModelSerializer):
    path = serializers.CharField(read_only=True)
    class Meta:
        model = TraceTxVizRequest
        fields = ('id', 'hash_index', 'created', 'completed', 'path')

class AddressVizRequestSerializer(serializers.ModelSerializer):
    path = serializers.CharField(read_only=True)
    class Meta:
        model = AddressVizRequest
        fields = ('id', 'address', 'tx_offset', 'tx_limit', 'comment','completed', 'created', 'path')

class SubcomponentSerializer(serializers.ModelSerializer):
    path = serializers.CharField(read_only=True)
    class Meta:
        model = Subcomponent
        fields = ('id','created', 'path', 'txs', 'txs_length')

class SubcomponentEmbedSerializer(serializers.ModelSerializer):
    path = serializers.CharField(read_only=True)
    class Meta:
        model = Subcomponent
        fields = ('id', 'path', 'txs_length')

class BlockVizRequestSerializer(serializers.ModelSerializer):
    path = serializers.CharField(read_only=True)
    #completed = serializers.BooleanField(read_only=True)

    subcomponents = SubcomponentEmbedSerializer(many=True, read_only=True)
    class Meta:
        model = BlockVizRequest
        fields = ('id', 'created', 'start', 'end', 'threshold', 'comment', 'path', 'completed', 'subcomponents')

class BlockVizSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockVizRequest
        fields = ('id','created', 'path', 'completed')
