from django.db import models
from django.contrib.auth.models import User
import hashlib
import os
from django.core.validators import RegexValidator
from django.utils import timezone
from main.models import *
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from decimal import Decimal
from main.choices import *

class Registration(models.Model):
    first_name = models.CharField(verbose_name="First Name",max_length=255,  blank=False)
    last_name = models.CharField(verbose_name="Last Name",max_length=255,  blank=False)
    email = models.EmailField(verbose_name="Email",max_length=255, blank=False)
    phone_number = models.CharField(blank=True, max_length=30, verbose_name="Phone number")
    country = models.CharField(max_length=255, verbose_name="Country", blank=False)
    date_inquired = models.DateTimeField(verbose_name="Date Inquired", default=timezone.now)
    name = models.CharField(verbose_name="Health Care Facility Name",max_length=255,  blank=False)
    district = models.CharField(verbose_name="District",max_length=255,  blank=False)
    accreditation = models.CharField(verbose_name="Accreditation Code",max_length=255,  blank=False)
    level = models.CharField(verbose_name="Level",max_length=255,choices=LEVEL_CHOICES, blank=False)
    
    objects = models.Manager() # The default manager.


    class Meta:
        verbose_name = "Registration"
        verbose_name_plural = "Registrations"

    def __str__(self):
        return self.full_name()
        #return "%s (%s)" % (self.first_name, self.last_name)

    def colored_name(self):
        from django.utils.html import format_html
        return format_html('<span style="color: #000;"><strong>{} {}<strong></span>',self.first_name,self.last_name)
    
    def full_name(self):
        return ', '.join([self.last_name, self.first_name])