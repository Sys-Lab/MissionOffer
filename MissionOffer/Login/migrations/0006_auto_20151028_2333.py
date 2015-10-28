# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0005_auto_20151023_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='edu',
            field=models.CharField(null=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='eval',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='phonenumber',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='realname',
            field=models.CharField(null=True, max_length=30),
        ),
    ]
