from django.shortcuts import render, redirect
from django.views.generic import View
from products.models import Recipe
class Index(View):
        """
        https://docs.djangoproject.com/en/1.9/topics/class-based-views/intro/
        """
        template_name = 'home/index.html'

        def get(self, request, *args, **kwargs):
            return render(request, self.template_name,)

        def post(self, request, *args, **kwargs):
            pass
