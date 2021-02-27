from django.urls import path
from .import views

from .views import (
    Waterworks_Zones,
    Waterworks_Zones_Table_AJAXView,
)

urlpatterns = [
    path('', Waterworks_Zones.as_view(), name = 'waterworks_zones'),
    path('api/table', Waterworks_Zones_Table_AJAXView.as_view(), name = 'waterworks_zones_table_api'),
]
