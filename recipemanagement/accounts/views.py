from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import View
from . models import Account
class Index(View):
    """
                    https://docs.djangoproject.com/en/1.9/topics/class-based-views/intro/
    """
    template_name = 'account/index.html'
    def get(self, request, *args, **kwargs):
        shipping = request.GET.get('q')
        print ("SADASDAasdasdsadsasadS")
        return render(request, self.template_name,)
    def post(self,request, *args, **kwargs):
        s = request.POST.get('q')
        p = request.POST.get('a')
        if s and p:
            current_user = request.user
            print (current_user.email)
            Account.objects.create(
                    s_address=s,
                    name=current_user.username,
                    f_name=current_user.first_name,
                    l_name = current_user.last_name,
                     price=p,
                    )
            return render(request, self.template_name,)
            print("SADASDASDSADSADSDSDSADASDSA")
        return render_to_response('home/index.html')
