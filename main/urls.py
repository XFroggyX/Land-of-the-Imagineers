from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers

from towns.views import TownCreateView
from . import views

router = routers.SimpleRouter()
router.register('api', TownCreateView, 'town')

urlpatterns = [
    url(r'login/', views.login_page),
    url(r'main/', include('field_game.urls')),
    url(r'sign_up/', views.sign_up)
]

urlpatterns += router.urls