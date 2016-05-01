from django.contrib import admin
from .models import stock,userstock
from django.contrib.auth.models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class stockResource(resources.ModelResource):

	class Meta:
		model = stock

class stockAdmin(ImportExportModelAdmin):
	list_display = ['name','code','price','max_price_of_day','update', 'stock_Exchange']
	search_fields = ('code',)
	resource_class = stockResource

class userStockResource(resources.ModelResource):
	class Meta:
		model  = userstock

class userStockAdmin(ImportExportModelAdmin):
	list_display = ['name','shares','balance']
	search_fields = ('name',)
	resource_class = userStockResource

admin.site.register(stock,stockAdmin)
admin.site.register(userstock,userStockAdmin)
