from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import (
    ProfileForm, UserRegistrationForm, ProfileEditForm, UserEditForm)


# Create your views here.
def accounts(request):
    return redirect('posts:dashboard')


def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            messages.success(request, 'Profile created successfully')
            return redirect('posts:dashboard')
    else:
        if request.user.is_authenticated():
            return render(request, 'registration/log_out_first.html')
        else:
            user_form = UserRegistrationForm()
            profile_form = ProfileForm()
    return render(
        request, "registration/registration.html", {
            'user_form': user_form, 'profile_form': profile_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(
            instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request, "accounts/edit.html", {
            'user_form': user_form, 'profile_form': profile_form})


@login_required
def profile(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})
