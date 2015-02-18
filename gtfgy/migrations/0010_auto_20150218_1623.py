# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuspknbh', '0008_auto_20150218_1623'),
        ('gtfgy', '0009_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rykamine',
            name='gwpcavl',
        ),
        migrations.AddField(
            model_name='yrekcfrkl',
            name='jnsjmikrnw',
            field=models.OneToOneField(null=True, related_name='+', to='cuspknbh.Djbbtxk'),
        ),
    ]
