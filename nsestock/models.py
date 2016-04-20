from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from decimal import Decimal
# Create your models here.

class stock(models.Model):
	name = models.CharField(max_length = 50)
	code = models.CharField(max_length = 10, unique = True)
	price = models.DecimalField(max_digits = 20, decimal_places = 4 , default = 00.00)
	max_price_of_day = models.DecimalField(max_digits= 20, decimal_places = 4, default = 00.00)
	change = models.CharField(max_length = 15,default = '0')

	def __unicode__(self):
		return self.name

class userstock(models.Model):
	name = models.ForeignKey(User)
	shares  = models.CharField(max_length =1000,default = "")
	balance = models.DecimalField(max_digits = 20, decimal_places = 4, default = 1000000.0000)

	def __unicode__(self):
		return self.name