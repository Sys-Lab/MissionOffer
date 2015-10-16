# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OfferMission', '0005_auto_20151016_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='status',
            field=models.CharField(default=0, max_length=10, choices=[('0', '待接收'), ('1', '进行中'), ('2', '已完成')]),
        ),
        migrations.AlterField(
            model_name='mission',
            name='type',
            field=models.CharField(default=0, max_length=20, choices=[('0', '寻找失物'), ('1', '食堂带饭'), ('2', '超市购物'), ('3', '文印中心'), ('4', '校外任务')]),
        ),
    ]
