from django.urls import path
from .import views

from .views import (
    Waterworks_Reading_Period_Detail,
    Waterworks_Reading_Period_Print,
)

urlpatterns = [
    path('<int:pk>', Waterworks_Reading_Period_Detail.as_view(), name = 'waterworks_reading_period_detail'),
    path('print/<int:pk>', Waterworks_Reading_Period_Print.as_view(), name = 'waterworks_reading_period_print'),
]
