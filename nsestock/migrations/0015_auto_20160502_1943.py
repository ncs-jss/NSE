# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('nsestock', '0014_auto_20160426_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstock',
            name='name',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userstock',
            name='shares',
            field=models.CharField(default=' ', max_length=1000),
        ),
    ]
