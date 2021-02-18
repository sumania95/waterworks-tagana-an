from django.urls import path
from .import views

from .views import (
    Waterworks_Home,
    Waterworks_Profile,
    Waterworks_Reading,
    Waterworks_Billing_Period,
    Waterworks_Barangay,
)

urlpatterns = [
    path('', Waterworks_Home.as_view(), name = 'waterworks_home'),
    path('profile', Waterworks_Profile.as_view(), name = 'waterworks_profile'),
    path('reading', Waterworks_Reading.as_view(), name = 'waterworks_reading'),
    path('billing-period', Waterworks_Billing_Period.as_view(), name = 'waterworks_billing_period'),
    path('barangay', Waterworks_Barangay.as_view(), name = 'waterworks_barangay'),
]
