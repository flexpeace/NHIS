from django import forms
from django.core.urlresolvers import reverse
from django.core import exceptions
from main.models import *
import logging
from django.core.exceptions import ValidationError
from django.core import exceptions
log = logging.getLogger(__name__)
from main.choices import *

class profileform(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        log.info("why")
        self.user = kwargs.pop("user", None)
        super(profileform, self).__init__(*args, **kwargs)
    
    def clean(self):
        super(profileform, self).clean()
        #self.cleaned_data['title']
        return self.cleaned_data
    
    #def save(self, request, commit=True,  *args, **kwargs):
        #m = super(inquiryForm, self).save(commit=False,  *args, **kwargs)
        #return m
    
  

    email = forms.EmailField(
        required=True,
        max_length=80,
        widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
    )
    
    country = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Country'}),
    )
    
    name = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name of Health Facility'}),
    )

    district = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'District'}),
    )

    accreditation = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Accreditation Code'}),
    )

    first_name = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'First name'}),
    )
    
    last_name = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Last name'}),
      
    )
    
    phone_number = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Phone number' }),
       
    )

    level = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'form-control '}),
        choices=LEVEL_CHOICES,
        #initial=TITLE_CHOICES[0][0],
    )
    
   
    class Meta:
        model = Registration
        exclude = ['date_inquired']



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')