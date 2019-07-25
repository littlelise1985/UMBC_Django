"""
URL Configuration for bands
"""
from django.urls import path
from django.shortcuts import get_object_or_404, render
from django.urls import path
from . import views   # import views from app

app_name = 'bands'

urlpatterns = [
    # add url patterns for the bands app here

    # Example:
    path('', views.home, name='home'),
    path('<str:band_name>', views.band_info, name='band_info'),
    path('band_list/', views.band_list, name='band_list'),
    path('band_detail/<str:band_name>', views.band_detail, name='band_detail'),
    path('band_sorted/', views.band_sorted, name='band_sorted'),
]

