from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.Index.as_view(), name='index'),
        url(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail.as_view(), name='recipe_detail'),
        url(r'^recipe/buy/(?P<pk>\d+)/$', views.recipe_buy.as_view(), name='recipe_buy'),
        url(r'^recipe/search', views.recipe_search.as_view(), name='recipe_search'),
       	url(r'^recipe/list', views.recipe_list.as_view(), name='recipe_list'),
     	]
