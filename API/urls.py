from django.conf.urls import url
from API import views

urlpatterns = [
    # Registering all the different view paths
    url(r'^API/BlockVizRequest/(?P<pk>[0-9]+)/$', views.BlockVizRequestDetail.as_view()),
    url(r'^API/BlockVizRequestList/$', views.BlockVizRequestList.as_view()),
    url(r'^API/Subcomponent/(?P<pk>[0-9]+)/$', views.SubcomponentDetail.as_view()),
    url(r'^API/SubcomponentList/$', views.SubcomponentList.as_view()),
    url(r'^API/BlockVizSearch/$', views.BlockVizSearch.as_view()),

    url(r'^API/AddressVizRequest/(?P<pk>[0-9]+)/$', views.AddressVizRequestDetail.as_view()),
    url(r'^API/AddressVizRequestList/$', views.AddressVizRequestList.as_view()),

    url(r'^API/TraceTxVizRequest/(?P<pk>[0-9]+)/$', views.TraceTxVizRequestDetail.as_view()),
    url(r'^API/TraceTxVizRequestList/$', views.TraceTxVizRequestList.as_view()),
]