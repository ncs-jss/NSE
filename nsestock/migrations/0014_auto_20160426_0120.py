# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsestock', '0013_auto_20160426_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstock',
            name='balance',
            field=models.FloatField(default=1000000.0),
        ),
    ]
