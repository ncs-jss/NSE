# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsestock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='max_price_of_day',
            field=models.DecimalField(default=0.0, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=20, decimal_places=4),
        ),
    ]
