from django.urls import path
from .import views

from .views import (
    Waterworks_Zones,
    Waterworks_Zones_Table_AJAXView,
    Waterworks_Zones_Cluster_AJAXView,
    Waterworks_Zones_Sequence_AJAXView,
)

urlpatterns = [
    path('', Waterworks_Zones.as_view(), name = 'waterworks_zones'),
    path('api/table', Waterworks_Zones_Table_AJAXView.as_view(), name = 'waterworks_zones_table_api'),
    path('api/table/cluster/<int:pk>', Waterworks_Zones_Cluster_AJAXView.as_view(), name = 'waterworks_zones_table_cluster_api'),
    path('api/table/sequence/<int:pk>', Waterworks_Zones_Sequence_AJAXView.as_view(), name = 'waterworks_zones_table_sequence_api'),
]
