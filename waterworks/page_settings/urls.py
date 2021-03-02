from django.urls import path
from .import views

from .views import (
    Waterworks_Settings,
    Waterwork_Settings_AJAXView,
    Waterwork_Modem_AJAXView,
)

urlpatterns = [
    path('', Waterworks_Settings.as_view(), name = 'waterworks_settings'),
    path('api/form/', Waterwork_Settings_AJAXView.as_view(), name = 'waterworks_settings_api'),
    path('api/modem/', Waterwork_Modem_AJAXView.as_view(), name = 'waterworks_modem_api'),
]
