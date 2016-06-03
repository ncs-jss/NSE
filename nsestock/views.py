from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import stock,userstock
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, Template
import json
# Create your views here.


class leaderboard(View):
	template = "leader.html"
	def get(self,request):
		participants = userstock.objects.all()
		leaders = []
		for user in participants:
			net_worth = user.balance
			try :
				jsonDec = json.decoder.JSONDecoder()
				user_shares = jsonDec.decode(user.shares)

				for share in user_shares:
					net_worth += (user_shares[share] * stock.objects.get(code = share).price)
			except :
				pass
			leaders += [{"name" : user.name.get_full_name(),'username':user.name.username, "worth" : net_worth}]
		leaders.sort(key=lambda x : x['worth'], reverse = True)
		return render(request, self.template, {'leaders':leaders})

class base(View):
	def get(self,request):
		return HttpResponseRedirect('/nse/')

class index(View):
	template = 'index.html'
	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(index, self).dispatch(*args, **kwargs)
	def get(self,request):	
		#if request.user.is_authenticated():
		stocks = stock.objects.all()
		shares = []
		try :
			blnce = 0		
			user = userstock.objects.get(name =request.user.id)
			jsonDec = json.decoder.JSONDecoder()
			user_shares = jsonDec.decode(user.shares)
		except :
			user_shares = {}
			
		for share in stocks:
			try:
				blnce = round(user.balance,2)
				quant = user_shares[share.code]
			except :
				quant = 0
			shares += [{"name":share.name, "price":round(share.price,2), "max":share.max_price_of_day, "code":share.code, "quant":quant}]
			
		return render(request,self.template,{'shares':shares,'blnce':blnce})
		# else :
		# 	return HttpResponseRedirect('/account/login/')
	def post(self,request):

		if request.POST.get('action') == "update":
			stocks = stock.objects.all()
			shares = []
			for share in stocks:
				shares += [{"name":share.name, "price":round(share.price,2), "max":round(share.max_price_of_day,2), "code":share.code}]

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
		try:
			quant = int(request.POST.get('quant'))
		except :
			return HttpResponse(json.dumps({'status':"enter a valid quantity"}),
				content_type = 'application/json')
		share = stock.objects.get(code = request.POST.get('code'))
		user = userstock.objects.get(name = request.user.id)
		response = {}
		try :
			jsonDec = json.decoder.JSONDecoder()
			user_shares = jsonDec.decode(user.shares)
		except :
			user_shares = {}
			response['status'] = "You don't have any share"
			return HttpResponse(json.dumps(response),
			content_type = 'application/json'
			)
		if share.code in user_shares and user_shares[share.code] >= quant:
			user.balance += (quant*share.price)
			user_shares[share.code] -= quant
			user.shares = json.dumps(user_shares)
			user.save()
			response['status'] = "sucess"
			response['blnce'] = user.balance
			response['quant'] = user_shares[share.code]
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
		try:
			quant = int(request.POST.get('quant'))
		except :
			return HttpResponse(json.dumps({'status':"enter a valid quantity"}),
				content_type = 'application/json')
		share = stock.objects.get(code = request.POST.get('code'))
		user = userstock.objects.get(name = request.user.id)
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
			response['quant'] = user_shares[share.code]
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