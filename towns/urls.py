from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'towns', views.TownViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', views.towns_list),
    path('<int:pk>', views.snippet_detail),
]

