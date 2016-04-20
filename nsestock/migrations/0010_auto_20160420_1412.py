# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsestock', '0009_auto_20160420_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='change',
        ),
        migrations.AddField(
            model_name='stock',
            name='update',
            field=models.IntegerField(default=0),
        ),
    ]
