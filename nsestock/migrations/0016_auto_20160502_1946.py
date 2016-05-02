# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsestock', '0015_auto_20160502_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstock',
            name='shares',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
