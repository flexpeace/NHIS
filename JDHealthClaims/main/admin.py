from django.contrib import admin
from django.contrib.auth.models import User
import logging
from django.core import exceptions
log = logging.getLogger(__name__)
from main.models import *


class registrationAdmin( admin.ModelAdmin):
    list_filter = [ 'level',]
    list_display = ['first_name', 'last_name','email', 'phone_number','country', 'country',  'level',]
    search_fields = [ 'first_name', 'last_name', 'email', 'phone_number']
    ordering = ['date_inquired']
    list_per_page = 100
    
admin.site.register(Registration, registrationAdmin)