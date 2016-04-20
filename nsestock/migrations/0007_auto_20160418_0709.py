# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsestock', '0006_auto_20160418_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstock',
            name='shares',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
