from django.urls import path
from .import views

from .views import (
    Waterworks_Reports,
    Waterworks_Reports_Table_AJAXView,
)

urlpatterns = [
    path('', Waterworks_Reports.as_view(), name = 'waterworks_reports'),
    path('api/table', Waterworks_Reports_Table_AJAXView.as_view(), name = 'waterworks_reports_table_api'),
]
