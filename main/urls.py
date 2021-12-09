from django.conf.urls import url
from rest_framework import routers

from .views import TownViewSet, towns_list, snippet_detail
from . import views

router = routers.SimpleRouter()
router.register(r'api', TownViewSet, 'town')
#router.register('api/list', towns_list.as_view(), 'town_list'),
#router.register('api/list/<int:pk>', snippet_detail.as_view(), 'town_detail')


urlpatterns = [
    url(r'login/', views.login_page),
    url(r'main/', views.main_page),
    url(r'sign_up/', views.sign_up),
    url('api/list', towns_list),
    url('api/list/<int:pk>', snippet_detail)
]

urlpatterns += router.urls