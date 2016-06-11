from django.shortcuts import render
from rest_framework import generics

from models import BlockVizRequest, Subcomponent
from serializers import BlockVizRequestSerializer, BlockVizSearchSerializer, SubcomponentSerializer

from models import AddressVizRequest
from serializers import AddressVizRequestSerializer

from models import TraceTxVizRequest
from serializers import TraceTxVizRequestSerializer

from django.views.generic import View
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.clickjacking import xframe_options_exempt

from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
# To fix lack of Xserver issue
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import mpld3
from graphing import Graphing


@xframe_options_exempt
def subcomponent_graph(request):
    id = request.GET.get('subcomponent', 114)
    title = "Subcomponent Graph"

    txs = Graphing.get_subcomponent_txs(id)

    address_count = {}
    for tx in txs:

        if str(tx.address) in address_count:
            address_count[str(tx.address)] += 1
        else:
            address_count[str(tx.address)] = 1

    count = []
    key = []

    for address in sorted(address_count):
        count.append(address_count[address])
        key.append(address)

    ind = np.arange(len(address_count))  # the x locations for the groups

    width = 0.8       # the width of the bars

    fig, ax = plt.subplots()
    ax.xaxis.set_tick_params(pad=15)

    boxes = ax.bar(ind, count, width, color='b')

    #ax.set_title(title, size=20)
    ax.set_ylabel('Transaction Count')
    ax.set_xlabel('Address')

    tooltip = None
    for i, box in enumerate(boxes.get_children()):
        tooltip = mpld3.plugins.LineLabelTooltip(box, label=key[i])
        mpld3.plugins.connect(fig, tooltip)

    mpld3.plugins.connect(fig, tooltip)
    g = mpld3.fig_to_html(fig)
    #mpld3.show()
    plt.close('all')
    return HttpResponse(g)

@xframe_options_exempt
def address_graph(request):
    id = request.GET.get('address_request', 43)
    query = AddressVizRequest.objects.get(pk=id)
    address = query.address
    offset = query.tx_offset
    limit = query.tx_limit

    title = address + " Transactions " + str(offset) + " to " + str(offset + limit)
    txs = Graphing.get_address_viz_txs(id)
    
    block_count = {}
    for tx in txs:

        if str(tx.block) in block_count:
            block_count[str(tx.block)] += 1
        else:
            block_count[str(tx.block)] = 1

    count = []
    key = []

    for block in sorted(block_count):
        count.append(block_count[block])
        key.append(block)

    ind = np.arange(len(block_count))  # the x locations for the groups

    width = 0.8       # the width of the bars

    fig, ax = plt.subplots()
    ax.xaxis.set_tick_params(pad=15)

    boxes = ax.bar(ind, count, width, color='b')

    ax.set_title(title, size=20)
    ax.set_ylabel('Transaction Count')
    ax.set_xlabel('Block')

    tooltip = None
    for i, box in enumerate(boxes.get_children()):
        tooltip = mpld3.plugins.LineLabelTooltip(box, label=key[i])
        mpld3.plugins.connect(fig, tooltip)

    mpld3.plugins.connect(fig, tooltip)
    g = mpld3.fig_to_html(fig)
    #mpld3.show()
    plt.close('all')
    return HttpResponse(g)


@xframe_options_exempt
def mempool_graph(request):
    id = request.GET.get('block_request', 100)
    query = BlockVizRequest.objects.get(pk=id)
    start = query.start
    end = query.end
    if end - start > 1:
        title = "Blocks [" + str(start) + ", " + str(end) + ")"
    else:
        title = "Block " + str(start)

    txs = Graphing.get_block_viz_txs(id)
    X = [float(tx.mempool_size)/float(1024*1024) for tx in txs]
    Y = [tx.confirmation_mins for tx in txs]

    fig, ax = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'))
    N = 100

    scatter = ax.scatter(X, Y)
    ax.grid(color='white', linestyle='solid')

    ax.set_title(title, size=20)
    ax.set_ylabel('Confirmation Time (mins)')
    ax.set_xlabel('Mempool Size (MB)')

    labels = [tx.hash for tx in txs]
    tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
    mpld3.plugins.connect(fig, tooltip)

    g = mpld3.fig_to_html(fig)
    #mpld3.show()
    plt.close('all')
    return HttpResponse(g)

@xframe_options_exempt
def fee_graph(request):
    id = request.GET.get('block_request', 100)
    query = BlockVizRequest.objects.get(pk=id)
    start = query.start
    end = query.end
    if end - start > 1:
        title = "Blocks [" + str(start) + ", " + str(end) + ")"
    else:
        title = "Block " + str(start)

    txs = Graphing.get_block_viz_txs(id)
    X = [tx.fee_per_byte for tx in txs]
    Y = [tx.confirmation_mins for tx in txs]

    fig, ax = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'))
    N = 100

    scatter = ax.scatter(X, Y)
    ax.grid(color='white', linestyle='solid')

    ax.set_title(title, size=20)
    ax.set_ylabel('Confirmation Time (mins)')
    ax.set_xlabel('Fee per byte (satoshi/byte)')

    labels = [tx.hash for tx in txs]
    tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
    mpld3.plugins.connect(fig, tooltip)

    g = mpld3.fig_to_html(fig)
    #mpld3.show()
    plt.close('all')
    return HttpResponse(g)

class TraceTxVizRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TraceTxVizRequest.objects.all()
    serializer_class = TraceTxVizRequestSerializer

class TraceTxVizRequestList(generics.ListCreateAPIView):
    queryset = TraceTxVizRequest.objects.all()
    serializer_class = TraceTxVizRequestSerializer

class AddressVizRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AddressVizRequest.objects.all()
    serializer_class = AddressVizRequestSerializer

class AddressVizRequestList(generics.ListCreateAPIView):
    queryset = AddressVizRequest.objects.all()
    serializer_class = AddressVizRequestSerializer

class SubcomponentList(generics.ListCreateAPIView):
    queryset = Subcomponent.objects.all()
    serializer_class = SubcomponentSerializer

class SubcomponentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcomponent.objects.all()
    serializer_class = SubcomponentSerializer

class BlockVizSearch(generics.ListCreateAPIView):
    queryset = Subcomponent.objects.all()
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
