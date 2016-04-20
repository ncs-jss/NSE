from django.shortcuts import render
from django.contrib.auth.models import User
from .models import stock,userstock
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
# Create your views here.

class index(View):
	"""docstring for index"""
	def get(self,request):
		return HttpResponse("home page")

