from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import logging
from django.core import exceptions
from django.core.mail import EmailMultiAlternatives
import re
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import *
import warnings
from django.views.generic.edit import FormMixin
import json
from django.views.generic.edit import *
from django.shortcuts import *
from django.template import RequestContext
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import (HttpResponseRedirect, Http404,
                         HttpResponsePermanentRedirect)
from django.views.generic.base import TemplateResponseMixin, View, TemplateView
from django.views.generic.edit import FormView
from main.forms import *
from main.models import *
from django.core import exceptions
from django.views.generic import DetailView, DeleteView, ListView,  UpdateView
log = logging.getLogger(__name__)
from django.contrib import auth
from django.contrib.auth.models import User


def loginview(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/")
    else:
        # Show an error page
        return HttpResponseRedirect("/")


def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/main")      


def confirm(request):
    return render(request, 'confirm.html')

class CreateClaim(CreateView):
    model = Claim
    form_class = claimformForm
    success_url = reverse_lazy("home")
    template_name = "claim.html"


    def dispatch(self, request,  **kwargs):
        #self.id = self.kwargs['id']
        return super(CreateClaim, self).dispatch(request,**kwargs)
    
    def get_form_kwargs(self):
        kwargs = super(CreateClaim, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
    
    def form_valid(self, form):

        try:
            getMed = HealthProfile.objects.get(owner=self.request.user)
        except HealthProfile.DoesNotExist:
            pass

        self.object = form.save()

        if not getMed:
            self.object.submitted_by = getMed.name
            self.object.save()


        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        #log.info(form.errors)
        return super(CreateClaim, self).form_invalid(form)

    def get_object(self, queryset=None):
        # Check if self.object is already set to prevent unnecessary DB calls
        if hasattr(self, 'object'):
            return self.object
        else:
            return super(CreateClaim, self).get_object(queryset)

    def get_context_data(self, **kwargs):
        context = super(CreateClaim, self).get_context_data(**kwargs)

        from django.utils.crypto import get_random_string
        uniqueID = get_random_string(length=13, allowed_chars='1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        context['uniqueID'] = uniqueID
        return context

claim = CreateClaim.as_view()



def main(request):
    return render(request, 'home.html')


def home(request):
    
    if request.user.is_authenticated():
        try:
            profile = HealthProfile.objects.get(owner=request.user)
            hasProfile = True
        except HealthProfile.DoesNotExist:
            profile = None
            hasProfile = False
    else:
        profile = None
        hasProfile = None


    return render(request, 'indexOne.html', {'hasProfile':hasProfile, 'profile':profile})

def forgot(request):
    return render(request, 'passwordreset.html')



class updateView(UpdateView):
    template_name = "update.html"
    model = HealthProfile
    form_class = profileform
    success_url = reverse_lazy("confirm")
    context_object_name = 'profile'


    def dispatch(self, request,  **kwargs):
        #self.id = self.kwargs['id']
        return super(updateView, self).dispatch(request,**kwargs)
    
    def get_form_kwargs(self):
        kwargs = super(updateView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save(self)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        log.info(form.errors)
        return super(updateView, self).form_invalid(form)

    def get_object(self, queryset=None):
        # Check if self.object is already set to prevent unnecessary DB calls
        if hasattr(self, 'object'):
            return self.object
        else:
            return super(updateView, self).get_object(queryset)

update_view = updateView.as_view()

class profileView(FormView):
    template_name = "registration.html"
    form_class = profileform
    success_url = reverse_lazy("confirm")

    def get_form_kwargs(self):
        kwargs = super(profileView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        log.info("valid")
        self.object = form.save(self.request)
        self.object.owner = self.request.user
        self.object.save()
        return super(profileView, self).form_valid(form)

    def form_invalid(self, form):
        log.info(form.errors)
        return super(profileView, self).form_invalid(form)
  
    def get_context_data(self, **kwargs):
        log.info("context")
        ret = super(profileView, self).get_context_data(**kwargs)
        return ret

profile_view = profileView.as_view()

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            
            user = auth.authenticate(username=user.username, password=user.password)
            if user is not None and user.is_active:
                # Correct password, and the user is marked "active"
                auth.login(request, user)
                # Redirect to a success page.
            return HttpResponseRedirect("/")

        else:
            print (user_form.errors)

    else:
        user_form = UserForm()
    return render_to_response( 'index.html',{'user_form': user_form, 'registered': registered}, context)