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
		u = User.objects.get(username = 'shivji')
		user = userstock.objects.get(name =u.id)
		for share in stocks:
			shares += [{"id":count,"name":share.name, "price":share.price, "max":share.max_price_of_day, "code":share.code}]
			count += 1
		return render(request,self.template,{'shares':shares,'blnce':user.balance})
	def post(self,request):
		if request.POST.get('action') == "update":
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
		else :
			return render(request,self.template, {})

class sell(View):
	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(sell, self).dispatch(*args, **kwargs)

	def get(self,request):
		return HttpResponse("this is only for api call")
	def post(self,request):
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
			response = {}
			response['status'] = "You don't have any share"
			return HttpResponse(
			json.dumps(response),
			content_type = 'application/json'
			)
		response = {}
		if share.code in user_shares and user_shares[share.code] >= quant:
			user.balance += (quant*share.price)
			user_shares[share.code] -= quant
			user.shares = json.dumps(user_shares)
			user.save()
			response['status'] = "sucess"
			response['blnce'] = user.balance
			return HttpResponse(json.dumps(response),
			content_type = 'application/json'
			)
		else :
			response['status'] = "You don't have sufficient quantity of share"
			return HttpResponse(json.dumps(response),
			content_type = 'application/json'
			)

class buy(View):
	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(buy, self).dispatch(*args, **kwargs)
	def get(self,request):
		return HttpResponse('This page is available only for api call')
	def post(self,request):
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
		response = {}
		if user.balance >= (quant*share.price):
			user.balance -= (quant*share.price)
			try :
				user_shares[share.code] += quant
			except :
				user_shares[share.code] = quant
			user.shares = json.dumps(user_shares)
			user.save()
			response['status'] = "sucess"
			response['blnce']  = user.balance
			return HttpResponse(
			json.dumps(response),
			content_type = 'application/json'
			)
		else :
			response['status'] = "You don't have sufficient money"
			return HttpResponse(
			json.dumps(response),
			content_type = 'application/json'
			)