from django.shortcuts import render
from rest_framework import generics

from models import BlockVizRequest

from serializers import BlockVizRequestSerializer

class BlockVizRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlockVizRequest.objects.all()
    serializer_class = BlockVizRequestSerializer

class BlockVizRequestList(generics.ListCreateAPIView):
    queryset = BlockVizRequest.objects.all()
    serializer_class = BlockVizRequestSerializer