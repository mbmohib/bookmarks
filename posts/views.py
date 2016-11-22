from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def post_list(request, user_id):
    post = UrlPost.objects.filter.all()
    return render(request, 'post_list.html', {'post': post})
