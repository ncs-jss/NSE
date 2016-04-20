# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsestock', '0008_stock_change'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student',
        ),
        migrations.AlterField(
            model_name='stock',
            name='change',
            field=models.IntegerField(default=0),
        ),
    ]
