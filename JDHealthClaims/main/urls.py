from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import CreateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView
urlpatterns = [
    # Examples:
     url(r'^$', 'main.views.home', name='home'),
   
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)