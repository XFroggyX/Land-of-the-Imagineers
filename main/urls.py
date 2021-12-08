from django.conf.urls import url
from rest_framework import routers

from .views import TownCreateView
from . import views

router = routers.SimpleRouter()
router.register('api', TownCreateView, 'town')

urlpatterns = [
    url(r'login/', views.login_page),
    url(r'main/', views.main_page),
    url(r'sign_up/', views.sign_up)
]

urlpatterns += router.urls