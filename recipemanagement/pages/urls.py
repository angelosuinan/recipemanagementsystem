from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.Index.as_view(), name='index'),
        url(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail.as_view(), name='recipe_detail'),
       	url(r'^recipe/', views.recipe_list.as_view(), name='recipe_list'),
     	]
