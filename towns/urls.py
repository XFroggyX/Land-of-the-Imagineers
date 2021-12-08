from django.urls import path, include
from .views import TownCreateView, index

from rest_framework import routers


router = routers.SimpleRouter()
router.register('api', TownCreateView, 'town')

urlpatterns = [
    path('', index, name='index'),
]

urlpatterns += router.urls


"""
    [
    #path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', towns_list),
    path('<int:pk>', snippet_detail),
]
"""
