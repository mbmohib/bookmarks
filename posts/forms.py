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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UrlPostForm, self).__init__(*args, **kwargs)
        self.fields['catagory'].queryset = Catagory.objects.filter(
                                    user=user)
