from django.contrib import admin
from .models import stock,userstock
from django.contrib.auth.models import User
# Register your models here.



admin.site.register(stock)
admin.site.register(userstock)
