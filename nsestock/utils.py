import threading
import ystockquote
from .models import stock
import traceback
import datetime
from nsetools import Nse

def update_shares_price():

	class nyse (threading.Thread):
	    def __init__(self, code):
	        threading.Thread.__init__(self)
	        self.code = code
	    def run(self):
	    	try :
	    		share = stock.objects.get(code=self.code)
	    		try :
	    			rate = float(ystockquote.get_price(share.code))
	    		except :
	    			print share.code
	    			return
	    		if share.price != rate:
	    			share.update = share.update +1
	    		share.price = rate
	    		if rate > share.max_price_of_day:
	    			share.max_price_of_day = rate
	    		share.save()
	    		print "sucess"
	    	except Exception,err:
	    		print err
	    		return		

	class nse (threading.Thread):
	    def __init__(self, code):
	        threading.Thread.__init__(self)
	        self.code = code
	    def run(self):
	    	try :
	    		share = stock.objects.get(code=self.code)
	    		nse = Nse()
	    		try :
	    			rate = nse.get_quote[self.code]
	    			rate = rate['lastPrice']
	    		except :
	    			print share.code
	    			return
	    		if share.price != rate:
	    			share.update = share.update +1
	    		share.price = rate
	    		if rate > share.max_price_of_day:
	    			share.max_price_of_day = rate
	    		share.save()
	    		print "sucess"
	    	except Exception,err:
	    		print err
	    		return			

	try :
	# check timing for stocks
		curr_time = datetime.datetime.now().time()
		nse_start_hour = 8
		nse_end_hour = 16
		nyse_start_hour = 19
		nyse_end_hour = 3
		print curr_time.hour
		if curr_time.hour >= nse_start_hour and curr_time.hour < nse_end_hour:
			# Create and run new thread
			all_stock = stock.objects.filter(stock_Exchange = "NSE")
			for share in all_stock:
				print share.stock_Exchange
				# thread = nse(share.code)
				# thread.start()
			
		elif curr_time.hour >= nyse_start_hour or curr_time.hour <= nyse_end_hour:
			# Create and run new thread
			all_stock = stock.objects.filter(stock_Exchange = "NYSE")
			for share in all_stock:
				print share.stock_Exchange
				# thread = nyse(share.code)
				# thread.start()
	except Exception,err:
		print err

def reset_max_shares_price():
	try :
		all_stock = stock.objects.all()[:11]
		for share in all_stock:
			share.max_price_of_day = 0.0
			share.save()
	except :
		reset_max_shares_price()
