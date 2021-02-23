from django.urls import path
from .import views

from .views import (
    Waterworks_Login,
    Waterworks_Logout,
)

urlpatterns = [
    path('login', Waterworks_Login.as_view(), name = 'waterworks_login'),
    path('logout', Waterworks_Logout.as_view(), name = 'waterworks_logout'),
]
