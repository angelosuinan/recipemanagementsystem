
from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'^$', views.Index.as_view(), name='index'),
            url(r'^signin/', views.signin.as_view(), name='signin'),
            
            url(r'^signup/process/', views.signup_process.as_view(), name='signup_process'),
            url(r'^signup/', views.signup.as_view(), name='signup'),
            url(r'^success/', views.success.as_view(), name='success'),
            url(r'^search/', views.search.as_view(), name='search')
            ]
