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
		paginator = Paginator(recipe_list, 9)
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
	def post(self, request, *args, **kwargs):
		query = self.request.POST.get('q')
		if len(query) < 4 :
			return render(request, 'home/index.html', )
		search = Recipe.objects.filter(name__contains=query)
		return render(request, 'recipe/recipe_list.html', {'recipes': search})
store = ""
class recipe_search(View):
	query = ""
	def get(self, request, *args, **kwargs):
		if self.request.GET.get('q'):
			self.query = self.request.GET.get('q')
			if len(self.query) < 4 :
				return render(request, 'home/index.html', )
			recipes_list = Recipe.objects.filter(name__contains=self.query)
			global store
			store = self.query
		else:
			recipes_list = Recipe.objects.filter(name__contains=store)
		paginator = Paginator(recipes_list, 9)
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
class recipe_buy(View):
    template='recipe/buy.html'
    def get (self, request, *args, **kwargs):
        #add if a user is login 
        if self.request.GET.getlist('products'):
            on = self.request.GET.getlist('products')
            context={}
            pk = kwargs.get('pk')
            recipe = get_object_or_404(Recipe, pk=pk)
            context ={}
            context['recipe'] = recipe
            products = recipe.products.all()
            x = 0
            p = []
            for product in products:
                print product
                if on[x]=='on':
                    p.append(product)
                x+=1
            context['products'] = p
            total =0
            for products in p:
                total += products.price
            context['total'] = total
        return render(request, self.template, context )
