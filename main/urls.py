from django.conf.urls import url
from django.conf.urls import include
from django.urls import include
from rest_framework import routers

from towns.views import user_count_view
from .views import TownViewSet, towns_list, snippet_detail, create_town, users_towns_list, StructTownViewSet, \
    UserViewSet, UserListViewSet
from . import views

router = routers.SimpleRouter()
router.register(r'town', TownViewSet, 'town')
router.register(r'struct', StructTownViewSet, 'town')
router.register(r'user', UserViewSet, 'town')
router.register(r'user_list', UserListViewSet, 'town')
# router.register('api/list', towns_list.as_view(), 'town_list'),
# router.register('api/list/<int:pk>', snippet_detail.as_view(), 'town_detail')


urlpatterns = [
    url(r'login/', views.login_page),
    url(r'main/', include('field_game.urls')),
    url(r'sign_up/', views.sign_up),
    url(r'check/', include("units.urls")),
    # url('api/user_list', users_towns_list),
    url('api/list', towns_list),
    url('api/list/<int:pk>', snippet_detail),
    url('api/', include(router.urls)),
    url('api/current_user', views.current_user)
    # url('api/struct/', user_town_list),
    # url('api/struct/<int:pk>', user_town_detail),
]

# urlpatterns += router.urls
