from django.shortcuts import render
from rest_framework import generics

from models import BlockVizRequest

from serializers import BlockVizRequestSerializer, BlockVizSearchSerializer

class BlockVizSearch(generics.ListCreateAPIView):
	queryset = BlockVizRequest.objects.all()
	serializer_class = BlockVizSearchSerializer

	def get_queryset(self):
		start     = self.request.query_params.get('start',     100000)
		end       = self.request.query_params.get('end'  ,     100001)
		threshold = self.request.query_params.get('threshold', 1000)

		queryset = BlockVizRequest.objects.filter(start=start,
			                                      end=end,
			                                      threshold=threshold)

		if len(queryset) < 1:
			queryset = BlockVizRequest.objects.create(start=start,
			                                          end=end,
			                                          threshold=threshold)
			queryset = BlockVizRequest.objects.filter(start=start,
			                                      end=end,
			                                      threshold=threshold)
		return queryset




class BlockVizRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlockVizRequest.objects.all()
    serializer_class = BlockVizRequestSerializer

class BlockVizRequestList(generics.ListCreateAPIView):
    queryset = BlockVizRequest.objects.all()
    serializer_class = BlockVizRequestSerializer
