from django.urls import path
from . import views

urlpatterns = [
    path("", views.init, name="menu-page"),
    path("<post_name>", views.get_post,name="inividual_post")
]
