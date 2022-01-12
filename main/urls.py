from django.conf.urls import url
from rest_framework import routers

from towns.views import user_count_view
from .views import TownViewSet, towns_list, snippet_detail, create_town, users_towns_list, StructTownViewSet
from . import views

router = routers.SimpleRouter()
router.register(r'api', TownViewSet, 'town')
router.register(r'api/struct', StructTownViewSet, 'townStruct')
#router.register('api/list', towns_list.as_view(), 'town_list'),
#router.register('api/list/<int:pk>', snippet_detail.as_view(), 'town_detail')


urlpatterns = [
    url(r'login/', views.login_page),
    url(r'main/', views.main_page),
    url(r'sign_up/', views.sign_up),
    url('api/user_list', users_towns_list),
    url('api/list', towns_list),
    url('api/list/<int:pk>', snippet_detail),
    url('api/create/<int:x, int:y>', create_town),
    #url('api/struct/', user_town_list),
    #url('api/struct/<int:pk>', user_town_detail),
]

urlpatterns += router.urls