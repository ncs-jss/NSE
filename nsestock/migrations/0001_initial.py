# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(max_digits=20, decimal_places=4)),
                ('max_price_of_day', models.DecimalField(max_digits=20, decimal_places=4)),
            ],
        ),
        migrations.CreateModel(
            name='userstock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shares', models.CharField(default='', max_length=25)),
                ('quate', models.CharField(default='', max_length=50)),
                ('balance', models.DecimalField(default=1000000.0, max_digits=20, decimal_places=4)),
                ('name', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
