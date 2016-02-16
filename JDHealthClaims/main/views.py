from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import logging
from django.core import exceptions
log = logging.getLogger(__name__)

def home(request):
    return render(request, 'index.html')

def forgot(request):
    return render(request, 'passwordreset.html')
