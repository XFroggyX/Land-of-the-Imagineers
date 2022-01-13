from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers

from .views import TownViewSet, towns_list, snippet_detail, create_town, users_towns_list
from . import views

router = routers.SimpleRouter()
router.register(r'api', TownViewSet, 'town')
#router.register('api/list', towns_list.as_view(), 'town_list'),
#router.register('api/list/<int:pk>', snippet_detail.as_view(), 'town_detail')


urlpatterns = [
    url(r'login/', views.login_page),
    url(r'main/', include('field_game.urls')),
    url(r'sign_up/', views.sign_up),
    url('api/user_list', users_towns_list),
    url('api/list', towns_list),
    url('api/list/<int:pk>', snippet_detail),
    url('api/create/<int:x, int:y>', create_town)
]

urlpatterns += router.urls