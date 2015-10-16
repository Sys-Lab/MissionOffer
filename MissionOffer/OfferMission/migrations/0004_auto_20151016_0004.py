# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OfferMission', '0003_auto_20151015_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='employee',
            field=models.ForeignKey(related_name='missionEmployee', to='Login.User', null=True, default=None),
        ),
    ]
