# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OfferMission', '0002_auto_20151015_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='employee',
            field=models.ForeignKey(to='Login.User', related_name='missionEmployee', default=None),
        ),
        migrations.AlterField(
            model_name='mission',
            name='offerTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
