
from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'^$', views.Index.as_view(), name='index'),
            url(r'^signin/', views.signin.as_view(), name='signin'),
            url(r'^signup.html/', views.signup.as_view(), name='signup'),
            url(r'^signup/process/', views.signup_process.as_view(), name='signup_process'),
            ]
