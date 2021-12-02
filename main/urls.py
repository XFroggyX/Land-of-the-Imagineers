from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'login/', views.login_page),
    url(r'main/', views.main_page),
    url(r'sign_up/', views.sign_up)
]