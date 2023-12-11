from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('puzzle_list', views.puzzle_list, name='puzzle_list'),
]