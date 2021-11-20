from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.template.loader import render_to_string
from django.urls import reverse

# Create your views here.
def init(request):
    return HttpResponse("this is the main page to view")

def index(request):
    return render(request, 'posts/index.html', {"data": 'data for main page'})

def get_post(request, post_name):
    return render(request, "posts/posts.html",{"data": "data for posts page"})
