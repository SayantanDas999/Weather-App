# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:01:38 2020

@author: Sayantan
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
]