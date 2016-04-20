# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsestock', '0002_auto_20160412_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='code',
            field=models.CharField(default='  ', max_length=10),
            preserve_default=False,
        ),
    ]
