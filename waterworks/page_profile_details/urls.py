from django.urls import path
from .import views

from .views import (
    Waterworks_Profile_Detail,
    Waterworks_Profile_Detail_Overview_AJAXView,
    Waterworks_Profile_Detail_Reading_AJAXView,
    Waterworks_Profile_Detail_Reading_Table_AJAXView,
    Waterworks_Profile_Detail_Collection_AJAXView,
    Waterworks_Profile_Detail_Collection_Table_AJAXView,
    Waterworks_Profile_Detail_Activity_AJAXView,
    Waterworks_Profile_Detail_Activity_Table_AJAXView,
)

urlpatterns = [
    path('<int:pk>', Waterworks_Profile_Detail.as_view(), name = 'waterworks_profile_detail'),
    path('api/overview/<int:pk>', Waterworks_Profile_Detail_Overview_AJAXView.as_view(), name = 'waterworks_profile_detail_overview_api'),
    path('api/reading/<int:pk>', Waterworks_Profile_Detail_Reading_AJAXView.as_view(), name = 'waterworks_profile_detail_reading_api'),
    path('api/reading/table/<int:pk>', Waterworks_Profile_Detail_Reading_Table_AJAXView.as_view(), name = 'waterworks_profile_detail_reading_table_api'),
    path('api/collection/<int:pk>', Waterworks_Profile_Detail_Collection_AJAXView.as_view(), name = 'waterworks_profile_detail_collection_api'),
    path('api/collection/table/<int:pk>', Waterworks_Profile_Detail_Collection_Table_AJAXView.as_view(), name = 'waterworks_profile_detail_collection_table_api'),
    path('api/activity/<int:pk>', Waterworks_Profile_Detail_Activity_AJAXView.as_view(), name = 'waterworks_profile_detail_activity_api'),
    path('api/activity/table/<int:pk>', Waterworks_Profile_Detail_Activity_Table_AJAXView.as_view(), name = 'waterworks_profile_detail_activity_table_api'),
]
