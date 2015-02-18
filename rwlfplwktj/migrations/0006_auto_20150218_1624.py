# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyfslutb', '0011_rfdhb'),
        ('rwlfplwktj', '0005_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thqldbdjm',
            name='zcwgna',
        ),
        migrations.AddField(
            model_name='thqldbdjm',
            name='wgnoqjqg',
            field=models.ForeignKey(null=True, related_name='+', to='tyfslutb.Djnppzsr'),
        ),
    ]
