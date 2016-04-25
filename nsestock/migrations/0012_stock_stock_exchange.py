# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsestock', '0011_auto_20160422_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stock_Exchange',
            field=models.CharField(default='NYSE', max_length=10),
        ),
    ]
