from django.contrib import admin

from .models import (
    Account,
    Barangay,
    Year,
    Classification,
    Classification_Rates,
    Profile,
    Reading_Period,
    Meter_Installation,
    Meter_Replace,
    Reading,
    Permanently_Disconnected,
    Modification_Charges,
    Collection_Charges,
    Collection_Charges_Cancelled,
    Activity_Logs,
    User_Logs,
)
admin.site.register(Classification)
admin.site.register(Classification_Rates)
admin.site.register(Account)
admin.site.register(Barangay)
admin.site.register(Year)
admin.site.register(Profile)
admin.site.register(Reading_Period)
admin.site.register(Meter_Installation)
admin.site.register(Meter_Replace)
admin.site.register(Reading)
admin.site.register(Permanently_Disconnected)
admin.site.register(Modification_Charges)
admin.site.register(Collection_Charges)
admin.site.register(Collection_Charges_Cancelled)
admin.site.register(Activity_Logs)
admin.site.register(User_Logs)
