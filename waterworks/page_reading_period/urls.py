from django.urls import path,include
from .import views

from .views import (
    Waterworks_Reading_Period,
    Waterworks_Reading_Period_Create,
    Waterworks_Reading_Period_Create_AJAXView,
    Waterworks_Reading_Period_Table_AJAXView,
    Waterworks_Reading_Period_Update,
    Waterworks_Reading_Period_Update_AJAXView,
    Waterworks_Reading_Period_Update_Save_AJAXView,
)

urlpatterns = [
    path('', Waterworks_Reading_Period.as_view(), name = 'waterworks_reading_period'),
    path('detail/',include('waterworks.page_reading_period_details.urls')),
    path('create', Waterworks_Reading_Period_Create.as_view(), name = 'waterworks_reading_period_create'),
    path('api/create', Waterworks_Reading_Period_Create_AJAXView.as_view(), name = 'waterworks_reading_period_create_api'),
    path('api/table', Waterworks_Reading_Period_Table_AJAXView.as_view(), name = 'waterworks_reading_period_table_api'),
    path('update/<int:pk>', Waterworks_Reading_Period_Update.as_view(), name = 'waterworks_reading_period_update'),
    path('api/update', Waterworks_Reading_Period_Update_AJAXView.as_view(), name = 'waterworks_reading_period_update_api'),
    path('api/update/save/<int:pk>', Waterworks_Reading_Period_Update_Save_AJAXView.as_view(), name = 'waterworks_reading_period_update_save_api'),

]
