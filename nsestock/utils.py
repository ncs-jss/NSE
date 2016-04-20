import threading
import ystockquote
from .models import stock
import traceback

def update_shares_price():

	class myThread (threading.Thread):
	    def __init__(self, name):
	        threading.Thread.__init__(self)
	        self.name = name
	    def run(self):
	    	try :
	    		share = stock.objects.get(code=self.name)
	    		rate = ystockquote.get_price(self.name)
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

	# Create and run new thread
	all_stock = stock.objects.all()
	for share in all_stock:
		thread = myThread(share.code)
		thread.start()

def reset_max_shares_price():
	try :
		all_stock = stock.objects.all()[:11]
		for share in all_stock:
			share.max_price_of_day = 0.0
			share.save()
	except :
		reset_max_shares_price()
