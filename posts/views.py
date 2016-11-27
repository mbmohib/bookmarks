from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def post_list(request, username):
    user = User.objects.get(username=username)
    catagories = user.user_cat.all()
    # for catagory in catagories:
    #     posts = catagory.urlpost_set.all()
    posts = user.user_post.all()
    return render(request, 'post_list.html', {
        'catagories': catagories, 'UrlPost': posts})
