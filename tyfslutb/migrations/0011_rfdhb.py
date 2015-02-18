# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyxbcga', '0008_auto_20150218_1624'),
        ('tyfslutb', '0010_auto_20150218_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rfdhb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jhuhmbj', models.ForeignKey(null=True, related_name='+', to='wyxbcga.Begquxerkm')),
            ],
        ),
    ]
