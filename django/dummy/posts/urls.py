from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main_page"),
    path('<post_name>', views.get_post, name="individual_post")
]