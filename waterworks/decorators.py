from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.mixins import AccessMixin

class LogoutIfNotAdministratorHRISMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        administrator = Administrator.objects.filter(user = self.request.user).count()
        if administrator == 0:
            logout(request)
            return redirect('waterworks_login')
        return super(LogoutIfNotAdministratorHRISMixin, self).dispatch(request, *args, **kwargs)
