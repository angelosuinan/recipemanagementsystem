from django.shortcuts import render, redirect
from django.views.generic import View
from products.models import Recipe
from django.http import HttpResponseRedirect
from .forms import DataForm

class Index(View):
	"""
	https://docs.djangoproject.com/en/1.9/topics/class-based-views/intro/
	"""
	template_name = 'home/index.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name,)

	def post(self, request, *args, **kwargs):
		if request.method == 'POST': 
			search_query = request.POST.get('search_box', None)
			print("dsadsadasd")
		print (search_query)
		if search_query:
			pass

		return render(request, self.template_name, )
