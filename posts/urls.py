from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'create-category/$', views.create_category, name='create_category'),
    url(r'create-post/$', views.create_post, name='create_post'),
    url(r'category-list/$', views.category_list, name='category_list'),
]
