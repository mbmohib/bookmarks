from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.Test, name='test'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^edit/$', views.edit, name='registration'),
    url('^', include('django.contrib.auth.urls')),
]
