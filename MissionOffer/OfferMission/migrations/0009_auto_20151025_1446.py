# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OfferMission', '0008_auto_20151022_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='status',
            field=models.CharField(default='0', choices=[('0', '待接收'), ('1', '进行中'), ('2', '待审核'), ('3', '已完成')], max_length=20),
        ),
    ]
