from django.urls import path
from .import views

from .views import (
    Waterworks_Barangay,
    Waterworks_Barangay_Create,
    Waterworks_Barangay_Create_AJAXView,
    Waterworks_Barangay_Table_AJAXView,
    Waterworks_Barangay_Update,
    Waterworks_Barangay_Update_AJAXView,
    Waterworks_Barangay_Update_Save_AJAXView,
    Waterworks_Barangay_Delete_AJAXView,
)

urlpatterns = [
    path('', Waterworks_Barangay.as_view(), name = 'waterworks_barangay'),
    path('create', Waterworks_Barangay_Create.as_view(), name = 'waterworks_barangay_create'),
    path('api/create', Waterworks_Barangay_Create_AJAXView.as_view(), name = 'waterworks_barangay_create_api'),
    path('api/table', Waterworks_Barangay_Table_AJAXView.as_view(), name = 'waterworks_barangay_table_api'),
    path('update/<int:pk>', Waterworks_Barangay_Update.as_view(), name = 'waterworks_barangay_update'),
    path('api/update', Waterworks_Barangay_Update_AJAXView.as_view(), name = 'waterworks_barangay_update_api'),
    path('api/update/save/<int:pk>', Waterworks_Barangay_Update_Save_AJAXView.as_view(), name = 'waterworks_barangay_update_save_api'),
    path('api/delete/<int:pk>', Waterworks_Barangay_Delete_AJAXView.as_view(), name = 'waterworks_barangay_delete_api'),
]
