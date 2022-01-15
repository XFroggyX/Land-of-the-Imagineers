from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path(r'map/', views.display_field),
    path(r'town/', views.display_town)
]
