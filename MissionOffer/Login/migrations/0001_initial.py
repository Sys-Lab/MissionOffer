# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=2)),
                ('edu', models.CharField(max_length=5)),
                ('password', models.CharField(max_length=30)),
                ('realname', models.CharField(max_length=20)),
                ('idNumber', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phonenumber', models.CharField(max_length=20)),
                ('eval', models.CharField(max_length=100)),
            ],
        ),
    ]
