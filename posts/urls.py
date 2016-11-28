from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'create-catagory/$', views.create_catagory, name='create_catagory'),
    url(r'create-post/$', views.create_post, name='create_catagory'),
]
