# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_auto_20151006_0639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('status', models.CharField(default='0', choices=[('0', '待接收'), ('1', '进行中'), ('2', '已完成')], max_length=20)),
                ('type', models.CharField(default='0', choices=[('0', '寻找失物'), ('1', '食堂带饭'), ('2', '超市购物'), ('3', '文印中心'), ('4', '校外任务')], max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('context', models.TextField(max_length=200)),
                ('reward', models.FloatField()),
                ('fine', models.FloatField()),
                ('offerTime', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('employee', models.ForeignKey(related_name='missionEmployee', null=True, to='Login.User')),
                ('employer', models.ForeignKey(related_name='missionEmployer', to='Login.User')),
            ],
        ),
    ]
