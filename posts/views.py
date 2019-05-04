from django.shortcuts import render
# from django.http import HttpResponse
from .models import Posts
# Create your views here.

def index(request):

    posts = Posts.objects.all()

    context = {
        'title': 'New Bloges',
        'posts': posts
    }

    return render(request, 'posts/index.htm',context)
    
def details(request, id):
    ID = Posts.objects.get(id = id)

    context = {
        'id': ID
    }

    return render(request, 'posts/details.htm',context)
