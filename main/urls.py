from django.conf.urls import url

from main.views.login_page import login_page
from main.views.main_page import main_page

urlpatterns = [
    url(r'^login/$', login_page),
    url(r'^main/$', main_page),
]
