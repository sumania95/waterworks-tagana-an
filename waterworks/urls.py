from django.urls import path,include
from .import views

from .views import (
    Waterworks_Home,
)

urlpatterns = [
    path('', Waterworks_Home.as_view(), name = 'waterworks_home'),
    path('profile/', include('waterworks.page_profile.urls')),
    path('zones/', include('waterworks.page_zones.urls')),
    path('reading/', include('waterworks.page_reading.urls')),
    path('barangay/',include('waterworks.page_barangay.urls')),
    path('classification/',include('waterworks.page_classification.urls')),
    path('reading-period/',include('waterworks.page_reading_period.urls')),
    path('year/',include('waterworks.page_year.urls')),
    path('settings/',include('waterworks.page_settings.urls')),
    path('reports/',include('waterworks.page_reports.urls')),
    path('users/',include('waterworks.page_users.urls')),
    path('auth/',include('waterworks.page_auth.urls')),
]
