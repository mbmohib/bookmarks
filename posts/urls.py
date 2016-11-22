from django.conf.urls import include, url

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
]
