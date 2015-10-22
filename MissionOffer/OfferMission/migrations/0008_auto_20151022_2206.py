# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OfferMission', '0007_attachment_originname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='type',
            field=models.CharField(choices=[('0', '寻找失物'), ('1', '食堂带饭'), ('2', '超市购物'), ('3', '文印中心'), ('4', '校外任务'), ('5', '其他')], default='0', max_length=20),
        ),
    ]
