# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OfferMission', '0006_auto_20151021_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='originName',
            field=models.CharField(null=True, max_length=256),
        ),
    ]
