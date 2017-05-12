from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.accueil, name='accueil'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^new_account', views.new_account, name='new_account'),
    url(r'^register/$', views.register, name='register'),
    url(r'^accounts/profile/$', views.my_account, name='my_account'),
]
