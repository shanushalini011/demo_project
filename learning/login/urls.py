from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from login import views
from django.conf import settings
from django.conf.urls.static import static

from . import views
import os

app_name ='login'

urlpatterns = [
   
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path("logout/", views.logout, name="logout"),
    # path("chart/", views.chart, name="chart"),
    
   
]
