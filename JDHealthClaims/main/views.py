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
from django.shortcuts import *
from django.template import RequestContext
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import (HttpResponseRedirect, Http404,
                         HttpResponsePermanentRedirect)
from django.views.generic.base import TemplateResponseMixin, View, TemplateView
from django.views.generic.edit import FormView
from main.forms import profileform, UserForm
from main.models import *
from django.core import exceptions
from django.views.generic import DetailView, DeleteView, ListView
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


def main(request):
    return render(request, 'home.html')


def home(request):
    return render(request, 'index.html')

def forgot(request):
    return render(request, 'passwordreset.html')

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
        form.save(self.request)
        return super(profileView, self).form_valid(form)

    def form_invalid(self, form):
        log.info("invalid")
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
            print user_form.errors

    else:
        user_form = UserForm()
    return render_to_response( 'index.html',{'user_form': user_form, 'registered': registered}, context)