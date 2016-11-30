
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import CategoryForm, UrlPostForm
from .models import Category


# Create your views here.
@login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'user': user})


def post_list(request, username):
    posts = []
    user = User.objects.get(username=username)
    categories = user.user_cat.all()
    for category in categories:
        posts.append(category.urlpost_set.filter(status='public'))
    return render(request, 'post_list.html', {
            'categories': categories, 'posts': posts})


@login_required
def all_post(request):
    posts = []
    user = request.user
    categories = user.user_cat.all()
    for category in categories:
        posts.append(category.urlpost_set.filter())
    return render(request, 'post_list.html', {
            'categories': categories, 'posts': posts})


@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'category_list.html', {
            'categories': categories})


@login_required
def create_category(request):
    if request.method == "POST":
        category_form = CategoryForm(request.POST, user=request.user)
        if category_form.is_valid():
            new_entry = category_form.save(commit=False)
            new_entry.user = request.user
            new_entry.save()
            messages.success(request, 'Category created successfully')
            return redirect('posts:category_list')
    else:
        category_form = CategoryForm()
    return render(
        request, 'category_form.html', {
            'category_form': category_form
        }
    )


@login_required
def create_post(request):
    if request.method == 'POST':
        post_form = UrlPostForm(request.POST, user=request.user)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            messages.success(request, 'Url stored successfully')
            return redirect('posts:dashboard')
    else:
        post_form = UrlPostForm(user=request.user, initial={'url': 'http://'})
    return render(request, 'create_post.html', {'post_form': post_form})
