from django.urls import path
from .import views

from .views import (
    Waterworks_Reading,
    Waterworks_Reading_Table_AJAXView,
)

urlpatterns = [
    path('', Waterworks_Reading.as_view(), name = 'waterworks_reading'),
    path('api/table', Waterworks_Reading_Table_AJAXView.as_view(), name = 'waterworks_reading_table_api'),
]
