# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digmcd', '0014_auto_20150218_1625'),
        ('rqwywo', '0006_auto_20150218_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahcgzunnb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jytvvd', models.ForeignKey(null=True, related_name='+', to='digmcd.Untgafvod')),
            ],
        ),
    ]
