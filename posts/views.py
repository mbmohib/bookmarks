
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

from .forms import CatagoryForm, UrlPostForm


# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def post_list(request, username):
    posts = []
    user = User.objects.get(username=username)
    catagories = user.user_cat.all()
    for catagory in catagories:
        posts.append(catagory.urlpost_set.all())
    return render(request, 'post_list.html', {
            'catagories': catagories, 'posts': posts})


@login_required
def create_catagory(request):
    if request.method == "POST":
        catagory_form = CatagoryForm(request.POST)
        if catagory_form.is_valid():
            new_entry = catagory_form.save(commit=False)
            new_entry.user = request.user
            new_entry.save()
        else:
            return HttpResponse("Error Occured")
    else:
        catagory_form = CatagoryForm()
    return render(
        request, 'catagory_form.html', {
            'catagory_form': catagory_form
        }
    )


@login_required
def create_post(request):
    if request.method == 'POST':
        post_form = UrlPostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.save()
        else:
            return HttpResponse("Error Occured")
    else:
        post_form = UrlPostForm()
    return render(request, 'create_post.html', {'post_form': post_form})
