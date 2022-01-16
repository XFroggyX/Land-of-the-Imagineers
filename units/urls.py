from django.conf.urls import url
from django.urls import path, include

from main.views import TownViewSet
from .views import index

from rest_framework import routers


urlpatterns = [
    url('', index, name='index'),
]
