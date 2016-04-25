from django.contrib import admin
from .models import stock,userstock
from django.contrib.auth.models import User
# Register your models here.

class stockAdmin(admin.ModelAdmin):
	list_display = ['name','code','price','max_price_of_day','update', 'stock_Exchange']


admin.site.register(stock,stockAdmin)
admin.site.register(userstock)
