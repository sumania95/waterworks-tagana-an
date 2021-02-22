from django.urls import path
from .import views

from .views import (
    Waterworks_Reports,
)

urlpatterns = [
    path('', Waterworks_Reports.as_view(), name = 'waterworks_reports'),
]
