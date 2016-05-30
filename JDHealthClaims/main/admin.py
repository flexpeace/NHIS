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
   
class claimAdmin( admin.ModelAdmin):
    list_filter = [ 'ClaimNumber',]
    list_display = ['ClaimNumber', 'scheme_name','DateofClaim',]
    search_fields = [ 'ClaimNumber', ]
    ordering = ['DateofClaim']
    list_per_page = 100

class medicineAdmin( admin.ModelAdmin):
    list_filter = [ 'Code',]
    list_display = ['Code', 'generic_name','Price_Unit', 'Price','level',]
    search_fields = [ 'Code', ]
    ordering = ['generic_name']
    list_per_page = 100

class patientAdmin( admin.ModelAdmin):
    list_filter = [ 'first_name',]
    list_display = ['first_name', 'last_name','birthdate', 'Age','hospital_record_number',]
    search_fields = [ 'first_name', ]

class claimProfileAdmin( admin.ModelAdmin):
    list_filter = [ 'first_name',]
    list_display = ['first_name', 'last_name','email', 'phone_number','country', 'country', ]
    search_fields = [ 'first_name', 'last_name', 'email', 'phone_number']
    ordering = ['date_inquired']
    list_per_page = 100

admin.site.register(claimProfile, claimProfileAdmin)
admin.site.register(HealthProfile, registrationAdmin)
admin.site.register(Claim, claimAdmin)
admin.site.register(Medicine, medicineAdmin)
admin.site.register(Patient, patientAdmin)