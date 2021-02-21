from django.urls import path
from .import views

from .views import (
    Waterworks_Year,
    Waterworks_Year_Create,
    Waterworks_Year_Create_AJAXView,
    Waterworks_Year_Table_AJAXView,
    Waterworks_Year_Activate_AJAXView,
)

urlpatterns = [
    path('', Waterworks_Year.as_view(), name = 'waterworks_year'),
    path('create', Waterworks_Year_Create.as_view(), name = 'waterworks_year_create'),
    path('api/create', Waterworks_Year_Create_AJAXView.as_view(), name = 'waterworks_year_create_api'),
    path('api/table', Waterworks_Year_Table_AJAXView.as_view(), name = 'waterworks_year_table_api'),
    path('api/activate/<int:pk>', Waterworks_Year_Activate_AJAXView.as_view(), name = 'waterworks_year_activate_api'),
]
