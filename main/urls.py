from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from battle.views import BattleListViewSet
from .views import TownViewSet, towns_list, snippet_detail,StructTownViewSet, \
    UserViewSet, UserListViewSet
from . import views

router = routers.SimpleRouter()
router.register(r'town', TownViewSet, 'town')
router.register(r'struct', StructTownViewSet, 'town')
router.register(r'user', UserViewSet, 'town')
router.register(r'user_list', UserListViewSet, 'town')
router.register(r'battle', BattleListViewSet, 'battle')


urlpatterns = [
    url(r'login/', views.login_page),
    url(r'main/', include('field_game.urls')),
    url(r'sign_up/', views.sign_up) ,
    url(r'check/', include("units.urls")),
    # url('api/user_list', users_towns_list),
    url('api/list', towns_list),
    url('api/list/<int:pk>', snippet_detail),
    url('api/', include(router.urls)),
    url('api/current_user', views.current_user),
]
