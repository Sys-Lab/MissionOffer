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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('offerTime', models.DateTimeField(auto_created=True)),
                ('status', models.CharField(max_length=10, choices=[(0, '待接收'), (1, '进行中'), (2, '已完成')])),
                ('title', models.CharField(max_length=50)),
                ('context', models.TextField(max_length=200)),
                ('reward', models.FloatField()),
                ('fine', models.FloatField()),
                ('deadline', models.DateTimeField()),
                ('employee', models.ForeignKey(related_name='missionEmployee', to='Login.User')),
                ('employer', models.ForeignKey(related_name='missionEmployer', to='Login.User')),
            ],
        ),
    ]
