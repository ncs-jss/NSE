from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, Template
from .forms import login_form,register_form
from django.contrib.auth import authenticate, login
# Create your views here.


class register(View):
	template = "login.html"
	def get(self,request):
		reg_form = register_form()
		log_form = login_form()
		return render(request, self.template, {'login':log_form, 'register':reg_form})
	def post(self,request):
		if 'register' in request.POST:
			form = register_form(request.POST)
			if form.is_valid():
				form.cleaned_data.pop('password2')
				User.objects.create_user(**form.cleaned_data)
				user = authenticate(username = form.cleaned_data['username'],password = form.cleaned_data['password'])
				login(request,user)
				return HttpResponseRedirect('/')
			else :
				errors = form.errors
				return render(request,self.template, {'error':errors,'register':form})
		else :
			form = login_form(request.POST)
			if form.is_valid():	
				username =  form.cleaned_data['username']
				password =  form.cleaned_data['password']
				user = authenticate(username = username,password = password)
				if user is not None :
					if user.is_active:
						login(request,user)
						return HttpResponseRedirect('/')
					else :
						return HttpResponse("User account is deactivated")
				else:
					return HttpResponse("user is not valid")
			else :
				return render(request, self.template, {'login':form})
