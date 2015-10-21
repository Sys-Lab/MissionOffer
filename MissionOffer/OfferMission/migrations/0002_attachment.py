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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('files', models.FileField(upload_to='uploadFiles/Attachments')),
                ('belongTo', models.ForeignKey(to='OfferMission.Mission', null=True)),
            ],
        ),
    ]
