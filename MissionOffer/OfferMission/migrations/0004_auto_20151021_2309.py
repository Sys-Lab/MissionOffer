# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OfferMission', '0003_auto_20151021_2308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mission',
            options={'ordering': ['-offerTime']},
        ),
    ]
