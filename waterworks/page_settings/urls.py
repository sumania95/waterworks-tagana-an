from django.urls import path
from .import views

from .views import (
    Waterworks_Settings,
)

urlpatterns = [
    path('', Waterworks_Settings.as_view(), name = 'waterworks_settings'),
]
