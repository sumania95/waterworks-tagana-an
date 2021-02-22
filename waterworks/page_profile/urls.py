from django.urls import path,include
from .import views

from .views import (
    Waterworks_Profile,
    Waterworks_Profile_Create,
    Waterworks_Profile_Create_AJAXView,
    Waterworks_Profile_Table_AJAXView,
    Waterworks_Profile_Update,
    Waterworks_Profile_Update_AJAXView,
    Waterworks_Profile_Update_Save_AJAXView,
    Waterworks_Profile_Meter_Installation_Create,
    Waterworks_Profile_Meter_Installation_Create_AJAXView,
    Waterworks_Profile_Meter_Installation_Create_Save_AJAXView,
    Waterworks_Profile_Meter_Replace_Create,
    Waterworks_Profile_Meter_Replace_Create_AJAXView,
    Waterworks_Profile_Meter_Replace_Create_Save_AJAXView,
)

urlpatterns = [
    path('', Waterworks_Profile.as_view(), name = 'waterworks_profile'),
    path('detail/',include('waterworks.page_profile_details.urls')),
    path('create', Waterworks_Profile_Create.as_view(), name = 'waterworks_profile_create'),
    path('api/create', Waterworks_Profile_Create_AJAXView.as_view(), name = 'waterworks_profile_create_api'),
    path('api/table', Waterworks_Profile_Table_AJAXView.as_view(), name = 'waterworks_profile_table_api'),
    path('update/<int:pk>', Waterworks_Profile_Update.as_view(), name = 'waterworks_profile_update'),
    path('api/update', Waterworks_Profile_Update_AJAXView.as_view(), name = 'waterworks_profile_update_api'),
    path('api/update/save/<int:pk>', Waterworks_Profile_Update_Save_AJAXView.as_view(), name = 'waterworks_profile_update_save_api'),
    path('meter-installation/<int:pk>', Waterworks_Profile_Meter_Installation_Create.as_view(), name = 'waterworks_profile_meter_installation_create'),
    path('api/meter-installation', Waterworks_Profile_Meter_Installation_Create_AJAXView.as_view(), name = 'waterworks_profile_meter_installation_create_api'),
    path('api/meter-installation/save/<int:pk>', Waterworks_Profile_Meter_Installation_Create_Save_AJAXView.as_view(), name = 'waterworks_profile_meter_installation_create_save_api'),
    path('meter-replace/<int:pk>', Waterworks_Profile_Meter_Replace_Create.as_view(), name = 'waterworks_profile_meter_replace_create'),
    path('api/meter-replace', Waterworks_Profile_Meter_Replace_Create_AJAXView.as_view(), name = 'waterworks_profile_meter_replace_create_api'),
    path('api/meter-replace/save/<int:pk>', Waterworks_Profile_Meter_Replace_Create_Save_AJAXView.as_view(), name = 'waterworks_profile_meter_replace_create_save_api'),
]
