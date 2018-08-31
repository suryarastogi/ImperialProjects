from django.conf.urls import url
from openapi import views

urlpatterns = [
    # Registering all the different view paths

    # Search for Heat Maps for geolocations, local and params
    url(r'^openapi/heatmapsearch/$', views.HeatMapSearch.as_view()),
    # Search for Postcode Heat Maps, for gp params
    url(r'^openapi/heatmappostcodesearch/$', views.HeatMapPostcodeSearch.as_view()),
    # Search for KNN Graphs
    url(r'^openapi/graphsearch/$', views.GraphSearch.as_view()),
    # Render for KNN Graphs
    url(r'^openapi/graphrender/$', views.graph_render),
    # Render for KNN Graphs
    url(r'^openapi/graphrenderios/$', views.graph_render_ios),

    # Route for list of heat map queries
    url(r'^openapi/gridsquaredatalist/$', views.GridSquareDataList.as_view()),
    
    # Route for individual query based on primary key index
    url(r'^openapi/graphquery/(?P<pk>[0-9]+)/$', views.GraphQueryDetail.as_view()),
    # Route for list of heat map queries
    url(r'^openapi/graphquerylist/$', views.GraphQueryList.as_view()),
    # Route for list of heat maps for queries
    url(r'^openapi/graphlist/$', views.PredictionGraphList.as_view()),
    # Route for list of points for heat maps
    url(r'^openapi/graphpointlist/$', views.PredictionGraphPointList.as_view()),
     
     # Route for individual query based on primary key index
     url(r'^openapi/heatmaplocalquery/(?P<pk>[0-9]+)/$', views.HeatMapLocalQueryDetail.as_view()),
     # Route for list of heat map queries
     url(r'^openapi/heatmaplocalquerylist/$', views.HeatMapLocalQueryList.as_view()),
     # Route for list of heat maps for queries
     url(r'^openapi/heatmaplocallist/$', views.HeatMapLocalList.as_view()),
     # Route for list of points for heat maps
     url(r'^openapi/heatmaplocalpointlist/$', views.HeatMapLocalPointList.as_view()),
     
     # Route for individual query based on primary key index
     url(r'^openapi/heatmappostcodequery/(?P<pk>[0-9]+)/$', views.HeatMapPostcodeQueryDetail.as_view()),
     # Route for list of heat map queries
     url(r'^openapi/heatmappostcodequerylist/$', views.HeatMapPostcodeQueryList.as_view()),
     # Route for list of heat maps for queries
     url(r'^openapi/heatmappostcodelist/$', views.HeatMapPostcodeList.as_view()),
     # Route for list of points for heat maps
     url(r'^openapi/heatmappostcodepointlist/$', views.HeatMapPostcodePointList.as_view()),
]
