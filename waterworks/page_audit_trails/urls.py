from django.urls import path
from .import views

from .views import (
    Waterworks_Audit_Trails,
)

urlpatterns = [
    path('', Waterworks_Audit_Trails.as_view(), name = 'waterworks_audit_trails'),
]
