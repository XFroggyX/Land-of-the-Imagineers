from django.conf.urls import url
from django.conf.urls import include

from . import views

urlpatterns = [
    url(r'login/', views.login_page),
    url(r'main/', include('field_game.urls')),
    url(r'sign_up/', views.sign_up)
]