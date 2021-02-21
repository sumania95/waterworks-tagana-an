from django.urls import path
from .import views

from .views import (
    Waterworks_Profile,
    Waterworks_Profile_Create,
    Waterworks_Profile_Create_AJAXView,
    Waterworks_Profile_Table_AJAXView,
    Waterworks_Profile_Update,
    Waterworks_Profile_Update_AJAXView,
    Waterworks_Profile_Update_Save_AJAXView,
)

urlpatterns = [
    path('', Waterworks_Profile.as_view(), name = 'waterworks_profile'),
    path('create', Waterworks_Profile_Create.as_view(), name = 'waterworks_profile_create'),
    path('api/create', Waterworks_Profile_Create_AJAXView.as_view(), name = 'waterworks_profile_create_api'),
    path('api/table', Waterworks_Profile_Table_AJAXView.as_view(), name = 'waterworks_profile_table_api'),
    path('update/<int:pk>', Waterworks_Profile_Update.as_view(), name = 'waterworks_profile_update'),
    path('api/update', Waterworks_Profile_Update_AJAXView.as_view(), name = 'waterworks_profile_update_api'),
    path('api/update/save/<int:pk>', Waterworks_Profile_Update_Save_AJAXView.as_view(), name = 'waterworks_profile_update_save_api'),
]
