from django.contrib import admin
from .models import stock,userstock,student
from django.contrib.auth.models import User
# Register your models here.



admin.site.register(stock)
admin.site.register(userstock)
admin.site.register(student)