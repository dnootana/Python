from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, response
from django.shortcuts import redirect
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    return HttpResponse("main page")

def init(request):
    try:
        return render(request, "posts/index.html", {"data":"data to send to page"})
    except:
        raise Http404()

def get_post(request, post_name):
    try:
        return render(request, "posts/posts.html", {"post_name": post_name, "data":"data to send to page"})
    except:
        raise Http404()