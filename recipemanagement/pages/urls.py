from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.Index.as_view(), name='index'),
        url(r'^products/recipe/', views.recipe_list.as_view(), name='recipe_list'),
     	]
