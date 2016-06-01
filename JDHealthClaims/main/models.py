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
from decimal import Decimal


class HealthProfile(models.Model):
    owner = models.ForeignKey(User, verbose_name='user', null=True)
    first_name = models.CharField(verbose_name="First Name", max_length=255,  blank=False)
    last_name = models.CharField(verbose_name="Last Name",max_length=255,  blank=False)
    email = models.EmailField(verbose_name="Email", default="info@info.com", max_length=255, blank=False)
    phone_number = models.CharField(blank=True, max_length=30, default="0240647463",verbose_name="Phone number")
    country = models.CharField(max_length=255, verbose_name="location", default="Ghana", blank=False)
    date_inquired = models.DateTimeField(verbose_name="Date Inquired", default=timezone.now)
    name = models.CharField(verbose_name="Health Care Facility Name",max_length=255,  blank=False)
    district = models.CharField(verbose_name="District",max_length=255,  blank=False, default="JIRAPA-LAMBUSSIE")
    accreditation = models.CharField(verbose_name="Accreditation Code",max_length=255,  blank=False)
    level = models.CharField(verbose_name="Provider Type",max_length=255,choices=LEVEL_CHOICES, blank=False)
   
    objects = models.Manager() # The default manager.


    class Meta:
        verbose_name = "Health Care Professional Profiles"
        verbose_name_plural = "Health Care Professional Profiles"

    def __str__(self):
        return self.full_name()
        #return "%s (%s)" % (self.first_name, self.last_name)

    def colored_name(self):
        from django.utils.html import format_html
        return format_html('<span style="color: #000;"><strong>{} {}<strong></span>',self.first_name,self.last_name)
    
    def full_name(self):
        return ', '.join([self.last_name, self.first_name])

class claimProfile(models.Model):
    owner = models.ForeignKey(User, verbose_name='user', null=True)
    staffID = models.CharField(verbose_name="Staff ID", max_length=255,  blank=False)
    first_name = models.CharField(verbose_name="First Name", max_length=255,  blank=False)
    last_name = models.CharField(verbose_name="Last Name",max_length=255,  blank=False)
    email = models.EmailField(verbose_name="Email", default="info@info.com", max_length=255, blank=False)
    phone_number = models.CharField(blank=True, max_length=30, default="0240647463",verbose_name="Phone number")
    country = models.CharField(max_length=255, verbose_name="location", default="Ghana", blank=False)
    date_inquired = models.DateTimeField(verbose_name="Date Inquired", default=timezone.now)
    district = models.CharField(verbose_name="District",max_length=255,  blank=False, default="JIRAPA-LAMBUSSIE")
    
    objects = models.Manager() # The default manager.


    class Meta:
        verbose_name = "Claim Manager Profile"
        verbose_name_plural = "Claim Manager Profiles"

    def __str__(self):
        return self.full_name()
        #return "%s (%s)" % (self.first_name, self.last_name)

    def colored_name(self):
        from django.utils.html import format_html
        return format_html('<span style="color: #000;"><strong>{} {}<strong></span>',self.first_name,self.last_name)
    
    def full_name(self):
        return ', '.join([self.last_name, self.first_name])


class Patient(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=255,  blank=True)
    last_name = models.CharField(verbose_name="Last Name",max_length=255,  blank=True)
    Age = models.IntegerField(blank=True, default=18, verbose_name="Age")
    birthdate = models.DateField(verbose_name="Birthdate",blank=True ) 
    hospital_record_number = models.CharField(verbose_name="Hospital Record No:",max_length=255,  blank=True, default="0000000")
    nhis_number = models.CharField(verbose_name="NHIS Number",max_length=255,  blank=True)
    gender = models.CharField(verbose_name="Gender",max_length=255,choices=GENDER_CHOICES, blank=True)
    birthdate = models.DateField(verbose_name="Expiry Date",blank=True ) 

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.first_name


class Medicine(models.Model):
    Code = models.CharField(verbose_name="Code", max_length=255,  blank=True)
    generic_name = models.CharField(verbose_name="Generic Name",max_length=255,  blank=True)
    Price_Unit = models.CharField(verbose_name="Price Unit",max_length=255,  blank=True)
    Price = models.DecimalField(blank=True,max_digits=20,decimal_places=4,default=Decimal('0.0000'), verbose_name="Price")
    level = models.CharField(verbose_name="Level of prescribing",max_length=255,choices=LEVEL_CHOICES, blank=True)

    class Meta:
        verbose_name = "Medcine"
        verbose_name_plural = "Medicines"

    def __str__(self):
        return self.Code


class Claim(models.Model):
    ClaimNumber = models.CharField(verbose_name="Claim Number", max_length=255,  blank=True)
    scheme_name = models.CharField(verbose_name="Scheme Name",max_length=255, default="JIRAPA DISTRICT NHIS", blank=True)
    DateofClaim = models.DateField(verbose_name="Date of Claim",blank=True ) 
    clientNHISNumber = models.DateField(verbose_name="Client NHIS number",blank=False ) 

    
    Client = models.ForeignKey(Patient, verbose_name="Client", null=True, blank=True)
    
    typeOfService = models.CharField(verbose_name="Type of service (i)",max_length=255,choices=SERVICE_CHOICES, blank=True)
    Pharamacy = models.BooleanField(verbose_name="Pharamacy", default=False)
    unbundled = models.BooleanField(verbose_name="Unbundled", default=False)
    all_inclusive = models.BooleanField(verbose_name="All Inclusive", default=False)

    outcome = models.CharField(verbose_name="Outcome",max_length=255,choices=OUTCOME_CHOICES, blank=True)
   
    first_visit_date = models.DateField(verbose_name="First Visit Date",blank=True , null=True,  max_length=255, ) 
    second_visit_date = models.DateField(verbose_name="Second Visit Date",blank=True, null=True,  max_length=255,  ) 
    third_visit_date = models.DateField(verbose_name="Third Visit Date",blank=True ,  null=True, max_length=255, ) 
    forth_visit_date = models.DateField(verbose_name="Fourth Visit Date",blank=True , null=True,  max_length=255, ) 
    durationDays = models.IntegerField(blank=True, max_length=30, default=0, verbose_name="Duration of Spell (Days)")
    
    attendance = models.CharField(verbose_name="Type of Attendance",max_length=255,choices=ATTENDANCE_CHOICES, blank=True)
    specialtyCode = models.CharField(verbose_name="Specialty Code", max_length=4,  blank=True)
    specialtyDescription = models.CharField(verbose_name="Specialty Description", max_length=255,  blank=True)
    
    procedureOneDescription = models.CharField(verbose_name="Precedure 1 Description",max_length=255,blank=True)
    procedureTwoDescription = models.CharField(verbose_name="Precedure 2 Description",max_length=255, blank=True)
    procedureThreeDescription = models.CharField(verbose_name="Precedure 3 Description",max_length=255, blank=True)
   
    procedureOne_date = models.DateField(verbose_name="Procedure 1 Date",blank=True,  null=True, max_length=255,  ) 
    procedureTwo_date = models.DateField(verbose_name="Procedure 2 Date",blank=True , null=True,  max_length=255, ) 
    procedureThree_date = models.DateField(verbose_name="Procedure 3 Date",blank=True ,  null=True, max_length=255, ) 
    
    GDRGOneprocedure = models.CharField(verbose_name="G-DRG Procedure 1",max_length=255,blank=True)
    GDRGTwoprocedure = models.CharField(verbose_name="G-DRG Procedure 2",max_length=255,blank=True)
    GDRGThreeprocedure = models.CharField(verbose_name="G-DRG Procedure 3",max_length=255, blank=True)

    diagOneDescription = models.CharField(verbose_name="diagnosis 1 Description",max_length=255, blank=True)
    diagTwoDescription = models.CharField(verbose_name="diagnosis 2 Description",max_length=255, blank=True)
    diagThreeDescription = models.CharField(verbose_name="diagnosis 3 Description",max_length=255, blank=True)
    diagFourDescription = models.CharField(verbose_name="diagnosis 4 Description",max_length=255, blank=True)
    
    diagOne_date = models.DateField(verbose_name="diagnosis 1 Date",blank=True,  null=True, max_length=255,  ) 
    diagTwo_date = models.DateField(verbose_name="diagnosis 2 Date",blank=True , null=True,  max_length=255, ) 
    diagThree_date = models.DateField(verbose_name="diagnosis 3 Date",blank=True ,  null=True, max_length=255, ) 
    diagFour_date = models.DateField(verbose_name="diagnosis 4 Date",blank=True ,  null=True, max_length=255, ) 
    
    GDRGOnediag = models.CharField(verbose_name="G-DRG diagnosis 1",max_length=255, blank=True)
    GDRGTwodiag = models.CharField(verbose_name="G-DRG diagnosis 2",max_length=255, blank=True)
    GDRGThreediag = models.CharField(verbose_name="G-DRG diagnosis 3",max_length=255, blank=True)
    GDRGFourdiag = models.CharField(verbose_name="G-DRG diagnosis 4",max_length=255, blank=True)


    medOneDescription = models.CharField(verbose_name="Medicine 1 Description",max_length=255, blank=True)
    medTwoDescription = models.CharField(verbose_name="Medicine 2 Description",max_length=255,blank=True)
    medThreeDescription = models.CharField(verbose_name="Medicine 3 Description",max_length=255, blank=True)
    medFourDescription = models.CharField(verbose_name="Medicine 4 Description",max_length=255, blank=True)
    medFiveDescription = models.CharField(verbose_name="Medicine 5 Description",max_length=255, blank=True)
    
    medCodeOne = models.CharField(verbose_name="Medicine Code 1", max_length=255,  blank=True)
    medCodeTwo = models.CharField(verbose_name="Medicine Code 2", max_length=255,  blank=True)
    medCodeThree = models.CharField(verbose_name="Medicine Code 3", max_length=255,  blank=True)
    medCodeFour = models.CharField(verbose_name="Medicine Code 4", max_length=255,  blank=True)
    medCodeFive = models.CharField(verbose_name="Medicine Code 5", max_length=255,  blank=True)
    
    medOnePrice = models.DecimalField(blank=True, max_digits=20,decimal_places=2,default=Decimal('0.00'), verbose_name="Medicine 1 Price")
    medTwoPrice = models.DecimalField(blank=True, max_digits=20,decimal_places=2,default=Decimal('0.00'), verbose_name="Medicine 2 Price")
    medThreePrice = models.DecimalField(blank=True,max_digits=20,decimal_places=2,default=Decimal('0.00'), verbose_name="Medicine 3 Price")
    medFourPrice = models.DecimalField(blank=True,max_digits=20,decimal_places=2,default=Decimal('0.00'), verbose_name="Medicine 4 Price")
    medFivePrice = models.DecimalField(blank=True,max_digits=20,decimal_places=4,default=Decimal('0.00'), verbose_name="Medicine 5 Price")

    medQTYone = models.IntegerField(blank=True, default=0, verbose_name="Medicine 1 Quantity")
    medQTYTwo = models.IntegerField(blank=True,  default=0, verbose_name="Medicine 2 Quantity")
    medQTYThree = models.IntegerField(blank=True, default=0, verbose_name="Medicine 3 Quantity")
    medQTYFour = models.IntegerField(blank=True,  default=0, verbose_name="Medicine 4 Quantity")
    medQTYFive = models.IntegerField(blank=True,  default=0, verbose_name="Medicine 5 Quantity")

    medOneTotal = models.DecimalField(blank=True, max_digits=20,decimal_places=4,default=Decimal('0.00'), verbose_name="Medicine 1 Total Cost")
    medTwoTotal = models.DecimalField(blank=True, max_digits=20,decimal_places=4,default=Decimal('0.00'), verbose_name="Medicine 2 Total Cost")
    medThreeTotal = models.DecimalField(blank=True,max_digits=20,decimal_places=4,default=Decimal('0.00'), verbose_name="Medicine 3 Total Cost")
    medFourTotal= models.DecimalField(blank=True,max_digits=20,decimal_places=4,default=Decimal('0.00'), verbose_name="Medicine 4 Total Cost")
    medFiveTotal= models.DecimalField(blank=True,max_digits=20,decimal_places=4,default=Decimal('0.00'), verbose_name="Medicine 4 Total Cost")

    medOne_date = models.DateField(verbose_name="Medicine 1 Date",blank=True,  null=True, max_length=255,  ) 
    medTwo_date = models.DateField(verbose_name="Medicine 2 Date",blank=True ,  null=True, max_length=255, ) 
    medThree_date = models.DateField(verbose_name="Medicine 3 Date",blank=True , null=True,  max_length=255, ) 
    medFour_date = models.DateField(verbose_name="Medicine 4 Date",blank=True ,  null=True, max_length=255, ) 
    medFive_date = models.DateField(verbose_name="Medicine 5 Date",blank=True ,  null=True, max_length=255, ) 
    
   
    class Meta:
        verbose_name = "Claim"
        verbose_name_plural = "Claims"


    def __str__(self):
        return self.ClaimNumber