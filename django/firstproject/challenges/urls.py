from django.urls import path

from . import views

urlpatterns = [
    #path("january", views.jan),
    path("", views.index, name='index'),
    path("<int:month_name>", views.monthly_challenge_by_number),
    path("<str:month_name>", views.monthly_challenge, name="month-challenge"),
    #path("february", views.feb),
]
