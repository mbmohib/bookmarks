from datetime import date

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy

from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if len(password2) < 8:
            raise forms.ValidationError("Passwords at least 8 charecters long")
        if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(
                email=email).exclude(username=username).count():
            raise forms.ValidationError(
                "A user with that email already exists")
        return email


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'address')
        labels = {
            'address': ugettext_lazy('Your Location'),
        }
        help_texts = {
            'date_of_birth': ugettext_lazy(
                    'Date format should be in: "year-month-date", \
                    Ex: 1995-02-15, Age must be more than 15 years'),
        }

    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        today = date.today()
        if (dob.year + 15, dob.month, dob.day) > (
                today.year, today.month, today.day):
            raise forms.ValidationError(
                'Must be at least 15 years old to register')
        return dob


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'address', 'profile_pic')
