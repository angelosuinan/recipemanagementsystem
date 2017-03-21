from django.shortcuts import render, redirect
from django.views.generic import View
from products.models import Recipe
from django.http import HttpResponseRedirect
from .forms import DataForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

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
		if search_query:
			pass
		return render(request, self.template_name,)

class signup(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'home/signup.html',)

class signup_process(View):
	def post(self, request, *args, **kwargs):
		if request.method == 'POST': 
			try:
				usern = self.request.POST.get('user', None)
				pwd = self.request.POST.get('pwd', None)
				fname = self.request.POST.get('fname', None)
				lname = self.request.POST.get('lname', None)
				email = self.request.POST.get('email', None)
				user = User.objects.create_user(usern, email, pwd)
				user.first_name = fname
				user.last_name = lname
				user.save()
				if(authenticate(username=usern, password=pwd)):
					return render(request, 'home/success.html',)
			except(IntegrityError):
				return render(request, 'home/error.html',)

class signin(View):
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			usern = self.request.POST.get('user', None)
			pwd = self.request.POST.get('pwd', None)
			user = authenticate(username=usern, password=pwd)
			if user is not None:
				login(request, user)
				return render(request, 'home/index.html', {'user': user})
			else:
				return render(request, 'home/error.html',) 
