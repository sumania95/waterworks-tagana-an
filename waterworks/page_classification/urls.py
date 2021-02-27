from django.urls import path,include
from .import views

from .views import (
    Waterworks_Classification,
    Waterworks_Classification_Create,
    Waterworks_Classification_Create_AJAXView,
    Waterworks_Classification_Table_AJAXView,
    Waterworks_Classification_Update,
    Waterworks_Classification_Update_AJAXView,
    Waterworks_Classification_Update_Save_AJAXView,
    Waterworks_Classification_Delete_AJAXView,
)

urlpatterns = [
    path('', Waterworks_Classification.as_view(), name = 'waterworks_classification'),
    path('detail/',include('waterworks.page_classification_details.urls')),
    path('create', Waterworks_Classification_Create.as_view(), name = 'waterworks_classification_create'),
    path('api/create', Waterworks_Classification_Create_AJAXView.as_view(), name = 'waterworks_classification_create_api'),
    path('api/table', Waterworks_Classification_Table_AJAXView.as_view(), name = 'waterworks_classification_table_api'),
    path('update/<int:pk>', Waterworks_Classification_Update.as_view(), name = 'waterworks_classification_update'),
    path('api/update', Waterworks_Classification_Update_AJAXView.as_view(), name = 'waterworks_classification_update_api'),
    path('api/update/save/<int:pk>', Waterworks_Classification_Update_Save_AJAXView.as_view(), name = 'waterworks_classification_update_save_api'),
    path('api/delete/<int:pk>', Waterworks_Classification_Delete_AJAXView.as_view(), name = 'waterworks_classification_delete_api'),
]
