# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OfferMission', '0004_auto_20151016_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='status',
            field=models.CharField(max_length=10, choices=[(0, '待接收'), (1, '进行中'), (2, '已完成')], default=0),
        ),
    ]
