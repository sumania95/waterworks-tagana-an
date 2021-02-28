from django.urls import path
from .import views

from .views import (
    Waterworks_Account,
    Waterworks_Account_Create,
    Waterworks_Account_Create_AJAXView,
    Waterworks_Account_Table_AJAXView,
)

urlpatterns = [
    path('', Waterworks_Account.as_view(), name = 'waterworks_account'),
    path('create', Waterworks_Account_Create.as_view(), name = 'waterworks_account_create'),
    path('api/create', Waterworks_Account_Create_AJAXView.as_view(), name = 'waterworks_account_create_api'),
    path('api/table', Waterworks_Account_Table_AJAXView.as_view(), name = 'waterworks_account_table_api'),
]
