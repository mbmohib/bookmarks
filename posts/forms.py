from django.forms import ModelForm
from .models import Category, UrlPost


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['title']


class UrlPostForm(ModelForm):

    class Meta:
        model = UrlPost
        fields = ['title', 'slug', 'url', 'status', 'note', 'category']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UrlPostForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(
                                    user=user)
