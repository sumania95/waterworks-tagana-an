from django.urls import path
from .import views

from .views import (
    Waterworks_Classification_Detail,
    Waterworks_Classification_Detail_Table_AJAXView,
)

urlpatterns = [
    path('<int:pk>', Waterworks_Classification_Detail.as_view(), name = 'waterworks_classification_detail'),
    path('api/<int:pk>', Waterworks_Classification_Detail_Table_AJAXView.as_view(), name = 'waterworks_classification_detail_table_api'),
]
