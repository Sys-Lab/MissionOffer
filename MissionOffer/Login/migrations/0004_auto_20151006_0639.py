# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_auto_20151006_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='realname',
            field=models.CharField(max_length=30),
        ),
    ]
