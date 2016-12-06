from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'create-category/$', views.create_category, name='create_category'),
    url(r'category-list/$', views.category_list, name='category_list'),
    url(r'(?P<id>\d+)/category-edit/$', views.category_edit, name='edit_category'),
    url(r'(?P<id>\d+)/category-delete/$', views.category_delete, name='delete_category'),
    url(r'create-post/$', views.create_post, name='create_post'),
    url(r'(?P<id>\d+)/edit-post/$', views.edit_post, name='edit_post'),
    url(r'(?P<id>\d+)/delete-post/$', views.delete_post, name='delete_post'),
    url(r'post-list/$', views.all_post, name='all_post'),
    url(r'(?P<id>\d+)/$', views.url_detail, name='detail'),
]
