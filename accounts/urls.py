from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.Test, name='test'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^edit/$', views.edit, name='edit'),
    url('^', include('django.contrib.auth.urls')),
]
