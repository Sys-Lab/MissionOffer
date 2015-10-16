# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OfferMission', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('files', models.FileField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='mission',
            name='type',
            field=models.CharField(choices=[(0, '寻找失物'), (1, '食堂带饭'), (2, '超市购物'), (3, '文印中心'), (4, '校外任务')], max_length=20, default=0),
        ),
        migrations.AddField(
            model_name='attachment',
            name='belongTo',
            field=models.ForeignKey(to='OfferMission.Mission'),
        ),
    ]
