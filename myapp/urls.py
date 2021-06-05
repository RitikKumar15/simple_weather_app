from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_details, name='home'),
    #path('result', views.weather_details, name='details'),
]
