# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsestock', '0003_stock_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstock',
            name='quate',
        ),
        migrations.AlterField(
            model_name='userstock',
            name='shares',
            field=models.CharField(default='', max_length=100),
        ),
    ]
