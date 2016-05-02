from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.contrib.auth.models import User
from .models import stock,userstock
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, Template
import json
# Create your views here.

class index(View):
	"""docstring for index"""
	def get(self,request):
		return HttpResponse("home page")

class leaderboard(View):
	def get(self,request):
		leader = userstock.objects.order_by('balance')
		return HttpResponse(leader)

class index(View):
	template = 'index.html'
	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(index, self).dispatch(*args, **kwargs)
	def get(self,request):
		stocks = stock.objects.all()
		shares = []
		count = 1
		for share in stocks:
			shares += [{"id":count,"name":share.name, "price":share.price, "max":share.max_price_of_day, "code":share.code}]
			count += 1
		return render(request,self.template,{'shares':shares})
	def post(self,request):
		if request.POST.get('action') == "update":
			print "update"
			stocks = stock.objects.all()
			shares = []
			count = 1
			for share in stocks:
				shares += [{"id":count,"name":share.name, "price":share.price, "max":share.max_price_of_day, "code":share.code}]
				count += 1
			return HttpResponse(
				json.dumps(shares),
				content_type = 'application/json'
			)
		elif request.POST.get('action') == "buy":
			try :
				quant = int(request.POST.get('quant'))
				share = stock.objects.get(code = request.POST.get('code'))
				user = None
				# if request.user.is_authenticated():
				# 	user = userstocks.objects.get(name = request.user.username)
				u = User.objects.get(username = 'shivji')
				user = userstock.objects.get(name =u.id)
				try :
					jsonDec = json.decoder.JSONDecoder()
					user_shares = jsonDec.decode(user.shares)
				except :
					user_shares = {}
				if user.balance >= (quant*share.price):
					user.balance -= (quant*share.price)
					try :
						user_shares[share.code] += quant
					except :
						user_shares[share.code] = quant
					user.shares = json.dumps(user_shares)
					user.save()
					response = {}
					response['status'] = "sucess"
					return HttpResponse(
					json.dumps(response),
					content_type = 'application/json'
					)
				else :
					response = {}
					response['status'] = "You don't have sufficient money"
					return HttpResponse(
					json.dumps(response),
					content_type = 'application/json'
					)
			except Exception,err :
				print err
				return HttpResponse(
					json.dumps(err),
					content_type = "application/json"
				)
		else :
			return render(request,self.template, {})



