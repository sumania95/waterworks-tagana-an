from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.mixins import AccessMixin
from .models import (
    Settings,
    Barangay,
    Year,
    Reading_Period,
)

#JSON AJAX
from django.template.loader import render_to_string
from django.http import JsonResponse

class ConfigurationRequired(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        data = dict()
        settings = Settings.objects.first()
        barangay = Barangay.objects.first()
        year = Year.objects.first()
        reading_period = Reading_Period.objects.first()
        if settings==None:
            context = {
                'message': "Settings Configuration!",
            }
            return render(request,"waterworks/dummy_file.html",context)
        if barangay == None:
            context = {
                'message': "No Barangay!",
            }
            return render(request,"waterworks/dummy_file.html",context)
        if year==None:
            context = {
                'message': "No Year Yet!",
            }
            return render(request,"waterworks/dummy_file.html",context)
        if reading_period==None:
            context = {
                'message': "No Reading Period Yet!",
            }
            return render(request,"waterworks/dummy_file.html",context)

        return super(ConfigurationRequired, self).dispatch(request, *args, **kwargs)
