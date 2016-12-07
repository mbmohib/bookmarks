
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import CategoryForm, UrlPostForm, CatedoryEditForm, UrlPostEditForm
from .models import Category, UrlPost


def home(request):
    return render(request, 'home.html')


# Create your views here.
@login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'user': user})


def post_list(request, username):
    posts = []
    rows = str(4)
    user = User.objects.get(username=username)
    categories = user.user_cat.all()
    for category in categories:
        posts.append(category.urlpost_set.filter(status='public'))
    return render(request, 'post_list.html', {
            'categories': categories, 'posts': posts, 'rows': rows})


@login_required
def all_post(request):
    posts = []
    user = request.user
    categories = user.user_cat.all()
    for category in categories:
        posts.append(category.urlpost_set.filter())
    return render(request, 'post_list_all.html', {
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
def category_edit(request, id):
    category = get_object_or_404(Category, id=id)
    category_edit_form = CatedoryEditForm(
            request.POST or None, instance=category)
    if category_edit_form.is_valid():
        new_entry = category_edit_form.save(commit=False)
        new_entry.save()
        messages.success(request, 'Category created successfully')
        return redirect('posts:category_list')
    return render(
        request, 'category_edit_form.html', {
            'category_edit_form': category_edit_form
        }
    )


@login_required
def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    messages.success(request, "Successfully Deleted")
    category.delete()
    return redirect('posts:category_list')


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


@login_required
def url_detail(request, id):
    post = get_object_or_404(UrlPost, id=id)
    return render(request, 'post_detail.html', {'post': post})


@login_required
def edit_post(request, id):
    post = get_object_or_404(UrlPost, id=id)
    url_post_edit_form = UrlPostEditForm(
            request.POST or None, instance=post)
    if url_post_edit_form.is_valid():
        new_entry = url_post_edit_form.save(commit=False)
        new_entry.save()
        messages.success(request, 'Post Updated successfully')
        return redirect(post.get_absolute_url())
    return render(
        request, 'url_post_edit_form.html', {
            'url_post_edit_form': url_post_edit_form
        }
    )


@login_required
def delete_post(request, id):
    post = get_object_or_404(UrlPost, id=id)
    post.delete()
    messages.success(request, "Successfully Deleted")
    return redirect('posts:all_post')
