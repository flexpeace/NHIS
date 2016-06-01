from django import forms
from django.core.urlresolvers import reverse
from django.core import exceptions
from main.models import *
import logging
from django.core.exceptions import ValidationError
from django.core import exceptions
log = logging.getLogger(__name__)
from main.choices import *
from django.core.exceptions import ObjectDoesNotExist


class profileform(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        log.info("why")
        self.user = kwargs.pop("user", None)
        super(profileform, self).__init__(*args, **kwargs)
    
    def clean(self):
       pass
    
    #def save(self, request, commit=True,  *args, **kwargs):
        #m = super(profileform, self).save(commit=False,  *args, **kwargs)
       
        #m.save()
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
        model = HealthProfile
        exclude = ['date_inquired', 'owner']



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class claimformForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(claimformForm, self).__init__(*args, **kwargs)
        #self.fields['Client'] = forms.ModelChoiceField(queryset= Patient.objects.all(),required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Client'}))
    
    def clean(self):
        cleaned_data = super(claimformForm, self).clean()

        medOneDescription = cleaned_data.get("medOneDescription")
        medTwoDescription = cleaned_data.get('medTwoDescription')
        medThreeDescription = cleaned_data.get('medThreeDescription')
        medFourDescription = cleaned_data.get('medFourDescription')
        medFiveDescription = cleaned_data.get('medFiveDescription')

        medCodeOne = cleaned_data.get('medCodeOne')
        medCodeTwo =cleaned_data.get('medCodeTwo')
        medCodeThree = cleaned_data.get('medCodeThree')
        medCodeFour = cleaned_data.get('medCodeFour')
        medCodeFive = cleaned_data.get('medCodeFive')

        medOnePrice = cleaned_data.get('medOnePrice')
        medCodeTwo = cleaned_data.get('medCodeTwo')
        medCodeThree = cleaned_data.get('medCodeThree')
        medCodeFour = cleaned_data.get('medCodeFour')
        medCodeFive = cleaned_data.get('medCodeFive')


        try:
            getMed = Medicine.objects.get(Code=medCodeOne , generic_name=medOneDescription)
        except Medicine.DoesNotExist:
            raise ValidationError('Medicine description & Code do not match in our list')

        if not getMed:
            raise ValidationError('Medicine description & Code do not match in our list')

        if not getMed.Price == medOnePrice:
             raise ValidationError('Medicine price 1 is not correct')

        return self.cleaned_data

    def clean_medOneDescription(self):
        medOneDescription = self.cleaned_data['medOneDescription']
        log.info('medOneDescription')
        try:
            getMed = Medicine.objects.get(generic_name=medOneDescription)
        except Medicine.DoesNotExist:
            raise ValidationError('Medical description is not in our list')

        if not getMed:
            raise ValidationError('Medical description is not in our list')

        return medOneDescription

    def clean_medTwoDescription(self):
        medOneDescription = self.cleaned_data['medTwoDescription']
        log.info('medOneDescription')
        try:
            getMed = Medicine.objects.get(generic_name=medOneDescription)
        except Medicine.DoesNotExist:
            raise ValidationError('Medical description is not in our list')

        if not getMed:
            raise ValidationError('Medical description is not in our list')

        return medOneDescription    

    def clean_medThreeDescription(self):
        medOneDescription = self.cleaned_data['medThreeDescription']
        log.info('medOneDescription')
        try:
            getMed = Medicine.objects.get(generic_name=medOneDescription)
        except Medicine.DoesNotExist:
            raise ValidationError('Medical description is not in our list')

        if not getMed:
            raise ValidationError('Medical description is not in our list')

        return medOneDescription

    def clean_medFourDescription(self):
        medOneDescription = self.cleaned_data['medFourDescription']
        log.info('medOneDescription')
        try:
            getMed = Medicine.objects.get(generic_name=medOneDescription)
        except Medicine.DoesNotExist:
            raise ValidationError('Medical description is not in our list')

        if not getMed:
            raise ValidationError('Medical description is not in our list')

        return medOneDescription

    def clean_medFiveDescription(self):
        medOneDescription = self.cleaned_data['medFiveDescription']
        log.info('medFiveDescription')
        try:
            getMed = Medicine.objects.get(generic_name=medOneDescription)
        except Medicine.DoesNotExist:
            raise ValidationError('Medical description is not in our list')

        if not getMed:
            raise ValidationError('Medical description is not in our list')

        return medOneDescription


    #-------------------------

    def clean_medCodeOne(self):
        medOneDescription = self.cleaned_data['medCodeOne']
        log.info('medOneDescription')
        try:
            getMed = Medicine.objects.get(Code=medOneDescription)
        except Medicine.DoesNotExist:
            raise ValidationError('Medical Code is not in our list')

        if not getMed:
            raise ValidationError('Medical Code is not in our list')

        return medOneDescription

    def clean_medCodeTwo(self):
        medOneDescription = self.cleaned_data['medCodeTwo']
        log.info('medOneDescription')
        try:
            getMed = Medicine.objects.get(Code=medOneDescription)
        except Medicine.DoesNotExist:
            raise ValidationError('Medical Code is not in our list')

        if not getMed:
            raise ValidationError('Medical Code is not in our list')

        return medOneDescription    

    def clean_medCodeThree(self):
        medOneDescription = self.cleaned_data['medCodeThree']
        log.info('medOneDescription')
        try:
            getMed = Medicine.objects.get(Code=medOneDescription)
        except Medicine.DoesNotExist:
            raise ValidationError('Medical Code is not in our list')

        if not getMed:
            raise ValidationError('Medical Code is not in our list')

        return medOneDescription

    def clean_medCodeFour(self):
        medOneDescription = self.cleaned_data['medCodeFour']
        log.info('medOneDescription')
        try:
            getMed = Medicine.objects.get(Code=medOneDescription)
        except Medicine.DoesNotExist:
            raise ValidationError('Medical Code is not in our list')

        if not getMed:
            raise ValidationError('Medical Code is not in our list')

        return medOneDescription

    def clean_medCodeFive(self):
        medOneDescription = self.cleaned_data['medCodeFive']
        log.info('medFiveDescription')
        try:
            getMed = Medicine.objects.get(Code=medOneDescription)
        except Medicine.DoesNotExist:
            raise ValidationError('Medical Code is not in our list')

        if not getMed:
            raise ValidationError('Medical Code is not in our list')

        return medOneDescription

    def clean_clientNHISNumber(self):

        medOneDescription = self.cleaned_data['clientNHISNumber']
        
        try:
            getMed = Patient.objects.get(nhis_number=medOneDescription)
        except Patient.DoesNotExist:
            raise ValidationError('NHIS number does not exist')

        log.info(getMed)
        if not getMed:
            raise ValidationError('NHIS number does not exist')

        return medOneDescription


    #-------------------------


    #def save(self, request, commit=True,  *args, **kwargs):
        #m = super(inquiryForm, self).save(commit=False,  *args, **kwargs)
        #return m
 
    ClaimNumber = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Claim Number'}),
    )


    scheme_name = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control','value':'JIRAPA DISTRICT NHIS', 'placeholder': 'scheme name'}),
    )


    DateofClaim = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'yyyy-mm-dd'}),
    )


    #Client = forms.ModelChoiceField(queryset= Patient.objects.all(),required=True,
    #widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Client'}) )


    clientNHISNumber = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Client NHIS Number'}),
    )

    typeOfService = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'form-control '}),
        choices=SERVICE_CHOICES,
        #initial=TITLE_CHOICES[0][0],
    )

    outcome = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'form-control '}),
        choices=OUTCOME_CHOICES,
        #initial=TITLE_CHOICES[0][0],
    )

    
    first_visit_date = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'yyyy-mm-dd'}),
    )


    attendance = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'form-control '}),
        choices=ATTENDANCE_CHOICES,
        #initial=TITLE_CHOICES[0][0],
    )

    medOneDescription = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
    )

    medTwoDescription = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
    )

    medThreeDescription = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
    )

    medFourDescription = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
    )

    medFiveDescription = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
    )

    medFiveDescription = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
    )

    medCodeOne = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Code'}),
    )

    medCodeTwo = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Code'}),
    )

    medCodeThree = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Code'}),
    )

    medCodeFour = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Code'}),
    )

    medCodeFive = forms.CharField(
        required=True,
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Code'}),
    )


    medOnePrice = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Price'}),
    )

    medTwoPrice = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Price'}),
    )

    medThreePrice = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Price'}),
    )

    medFourPrice = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Price'}),
    )

    medFivePrice = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Price'}),
    )


    medQTYone = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Quantity'}),
    )

    medQTYTwo = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Quantity'}),
    )

    medQTYThree = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Quantity'}),
    )

    medQTYFour = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Quantity'}),
    )

    medQTYFive = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Quantity'}),
    )

    medOne_date = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Date yyyy-mm-dd'}),
    )

    medTwo_date = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Date yyyy-mm-dd'}),
    )

    medThree_date= forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Date yyyy-mm-dd'}),
    )

    medFour_date = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Date yyyy-mm-dd'}),
    )

    medFive_date = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicne Date yyyy-mm-dd'}),
    )

    medOneTotal = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={'readonly':'readonly','class': 'form-control', 'placeholder': 'Medicne Total Price'}),
    )

    medTwoTotal = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={'readonly':'readonly','class': 'form-control', 'placeholder': 'Medicne Total Price'}),
    )

    medThreeTotal = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={'readonly':'readonly','class': 'form-control', 'placeholder': 'Medicne Total Price'}),
    )

    medFourTotal = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={'readonly':'readonly','class': 'form-control', 'placeholder': 'Medicne Total Price'}),
    )

    medFiveTotal = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={'readonly':'readonly','class': 'form-control', 'placeholder': 'Medicne Total Price'}),
    )


    procedureOneDescription = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Procedure Description'}),
    )

    procedureTwoDescription = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Procedure Description'}),
    )

    procedureThreeDescription = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Procedure Description'}),
    )

    procedureOne_date= forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Procedure Date yyyy-mm-dd'}),
    )

    
    procedureTwo_date= forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Procedure Date yyyy-mm-dd'}),
    )

    procedureThree_date= forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Procedure Date yyyy-mm-dd'}),
    )


    GDRGOneprocedure = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GDRG'}),
    )

    GDRGTwoprocedure = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GDRG'}),
    )

    GDRGThreeprocedure = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GDRG'}),
    )

    diagOneDescription = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diagnosis Discription'}),
    )

    diagTwoDescription = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diagnosis Discription'}),
    )

    diagThreeDescription = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diagnosis Discription'}),
    )

    diagFourDescription = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diagnosis Discription'}),
    )

    diagOne_date= forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diagnosis Date yyyy-mm-dd'}),
    )

    
    diagTwo_date= forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diagnosis Date yyyy-mm-dd'}),
    )

    diagThree_date= forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diagnosis Date yyyy-mm-dd'}),
    )

    diagFour_date= forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diagnosis Date yyyy-mm-dd'}),
    )

  
    GDRGOnediag = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GDRG'}),
    )

    GDRGTwodiag = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GDRG'}),
    )

    GDRGThreediag = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GDRG'}),
    )

    GDRGFourdiag = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GDRG'}),
    )


    class Meta:
        model = Claim
        fields = '__all__' 

