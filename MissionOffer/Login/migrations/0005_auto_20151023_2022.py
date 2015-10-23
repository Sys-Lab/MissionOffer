# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_auto_20151006_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='authKey',
            field=models.CharField(null=True, max_length=45),
        ),
        migrations.AddField(
            model_name='user',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]
