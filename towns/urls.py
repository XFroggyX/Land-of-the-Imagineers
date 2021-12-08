from django.urls import path, include
from .views import TownViewSet, towns_list, snippet_detail

from rest_framework import routers


router = routers.DefaultRouter()
router.register('town', TownViewSet, 'town')

urlpatterns = router.urls

"""
    [
    #path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', towns_list),
    path('<int:pk>', snippet_detail),
]
"""
