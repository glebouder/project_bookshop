from django.conf.urls import url
from django.contrib.auth import views as auth_views #(??)
from . import views

urlpatterns = [
    url(r'^commandes/search/$', views.search, name="search"),
    url(r'^commandes/answer/(\d+)/$', views.answer, name="search"),
    url(r'^add/$', views.add, name="add"),
    url(r'^add/(.+)/$', views.add_sth, name = 'add_sth'),
]
