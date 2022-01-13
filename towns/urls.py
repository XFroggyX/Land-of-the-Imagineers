from django.conf.urls import url
from django.urls import path, include

from main.views import TownViewSet
from .views import index, user_count_view

from rest_framework import routers

#router.register('api', TownCreateView, 'town')

urlpatterns = [
    url('', index, name='index'),
]


"""
    [
    #path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', towns_list),
    path('<int:pk>', snippet_detail),
]
"""
