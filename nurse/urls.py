from django.shortcuts import render
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path("",signin),
    path("home",home,name = "home"),
    path("getreport",getreport),
    path("withdraw",withdraw),
    path("details<int:pk>",details,name = "ndetails")
]
