from django.forms import ModelForm
from .models import Category, UrlPost
from django import forms


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['title', 'sub_cat']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CategoryForm, self).__init__(*args, **kwargs)

    def clean(self):
        try:
            Category.objects.get(
                    title=self.cleaned_data['title'], user=self.user)
            raise forms.ValidationError("Exists already!")
        except Category.DoesNotExist:
            pass
        return self.cleaned_data


class UrlPostForm(ModelForm):

    class Meta:
        model = UrlPost
        fields = ['title', 'url', 'status', 'note', 'category']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UrlPostForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(
                                    user=user)


class CatedoryEditForm(ModelForm):

    class Meta:
        model = Category
        fields = ['title']


class UrlPostEditForm(ModelForm):

    class Meta:
        model = UrlPost
        fields = ['title', 'url', 'status', 'note', 'category']
