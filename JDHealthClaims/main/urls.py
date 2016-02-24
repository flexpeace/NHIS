from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import CreateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

admin.site.site_header = 'JD Health Claims'


urlpatterns = [
    # Examples:
     url(r'^$', 'main.views.home', name='home'),

        url(r'^forgot$', 'main.views.forgot', name='forgot'),
        url(r'^confirm$', 'main.views.confirm', name='confirm'),

         url(r'^main$', 'main.views.main', name='main'),
          url(r'^why$', 'main.views.loginview', name='loginview'),

 url(r'^signup$', 'main.views.register', name='register'),
 
      url(r'^registration$', 'main.views.profile_view', name='profile_view'),

 

   url( r'^login/$','django.contrib.auth.views.login', name='login', kwargs={'template_name': 'index.html'}),

    url(
        r'^logout/$','django.contrib.auth.views.logout', name='logout',
        kwargs={'next_page': '/'}
    ),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)