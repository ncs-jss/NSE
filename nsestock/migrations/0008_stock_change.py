# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsestock', '0007_auto_20160418_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='change',
            field=models.CharField(default='0', max_length=15),
        ),
    ]
