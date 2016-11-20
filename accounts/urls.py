from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.Test, name='test'),
    url(r'^registration/$', views.registration, name='registration'),
    url('^', include('django.contrib.auth.urls')),
]
