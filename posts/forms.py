from django.forms import ModelForm
from .models import Catagory, UrlPost


class CatagoryForm(ModelForm):

    class Meta:
        model = Catagory
        fields = ['title']


class UrlPostForm(ModelForm):

    class Meta:
        model = UrlPost
        fields = ['title', 'slug', 'url', 'status', 'note', 'catagory']
