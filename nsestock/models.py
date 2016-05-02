from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.


class stock(models.Model):
	name = models.CharField(max_length = 50)
	code = models.CharField(max_length = 10, unique = True, primary_key = True)
	price = models.FloatField(default = 00.00)
	max_price_of_day = models.FloatField(default = 00.00)
	stock_Exchange = models.CharField(max_length = 10, default = 'NYSE')
	update = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.name

class userstock(models.Model):
	name = models.OneToOneField(User)
	shares  = models.CharField(max_length =10000,default = "",)
	balance = models.FloatField(default = 1000000.0000)

	def __unicode__(self):
		return str(self.name)

