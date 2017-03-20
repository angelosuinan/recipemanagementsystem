from products.models import Recipe, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.shortcuts import render, redirect
from django.views.generic import View

class Index(View):
    """
            https://docs.djangoproject.com/en/1.9/topics/class-based-views/intro/
    """
    template_name = 'home/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,)
    def post(self, request, *args, **kwargs):
        pass

class recipe_list(View):
	def get(self, request, *args, **kwargs):
		recipe_list = Recipe.objects.all()
		paginator = Paginator(recipe_list, 10)
		page = request.GET.get('page')
		try:
		    recipes = paginator.page(page)
		except PageNotAnInteger:
		    # If page is not an integer, deliver first page.
		    recipes = paginator.page(1)
		except EmptyPage:
		    # If page is out of range (e.g. 9999), deliver last page of results.
		    recipes = paginator.page(paginator.num_pages)
		return render(request, 'recipe/recipe_list.html', {'recipes': recipes})


class recipe_detail(View):
	template_name = 'home/index.html'
	def get(self,request, *args, **kwargs):
		pk = kwargs.get('pk')
		recipe = get_object_or_404(Recipe, pk=pk)
		context = {}
		context['recipe'] = recipe
		context['products'] = recipe.products.all()
		return render(request, 'recipe/recipe_detail.html', context)