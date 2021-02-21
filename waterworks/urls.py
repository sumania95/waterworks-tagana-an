from django.urls import path,include
from .import views

from .views import (
    Waterworks_Home,
)

urlpatterns = [
    path('', Waterworks_Home.as_view(), name = 'waterworks_home'),
    path('profile/', include('waterworks.page_profile.urls')),
    path('reading/', include('waterworks.page_reading.urls')),
    path('barangay/',include('waterworks.page_barangay.urls')),
    path('reading-period/',include('waterworks.page_reading_period.urls')),
    path('year/',include('waterworks.page_year.urls')),
]
