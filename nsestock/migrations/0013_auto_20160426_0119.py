# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsestock', '0012_stock_stock_exchange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='max_price_of_day',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
