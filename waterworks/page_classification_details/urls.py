from django.urls import path
from .import views

from .views import (
    Waterworks_Classification_Detail,
    Waterworks_Classification_Detail_Table_AJAXView,
    Waterworks_Classification_Detail_Create_AJAXView,
    Waterworks_Classification_Detail_Update_AJAXView,
    Waterworks_Classification_Detail_Delete_AJAXView,
)

urlpatterns = [
    path('<int:pk>', Waterworks_Classification_Detail.as_view(), name = 'waterworks_classification_detail'),
    path('api/<int:pk>', Waterworks_Classification_Detail_Table_AJAXView.as_view(), name = 'waterworks_classification_detail_table_api'),
    path('api/create/<int:pk>', Waterworks_Classification_Detail_Create_AJAXView.as_view(), name = 'waterworks_classification_detail_create_api'),
    path('api/update/<int:pk>', Waterworks_Classification_Detail_Update_AJAXView.as_view(), name = 'waterworks_classification_detail_update_api'),
    path('api/delete/<int:pk>', Waterworks_Classification_Detail_Delete_AJAXView.as_view(), name = 'waterworks_classification_detail_delete_api'),
]
