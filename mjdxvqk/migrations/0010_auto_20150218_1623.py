# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtfgy', '0011_auto_20150218_1623'),
        ('mjdxvqk', '0009_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vmnilim',
            name='vkvsbd',
        ),
        migrations.RemoveField(
            model_name='edugsywcj',
            name='nvhgs',
        ),
        migrations.RemoveField(
            model_name='gedwra',
            name='utpyfgmizz',
        ),
        migrations.AddField(
            model_name='curcmm',
            name='gasoypwn',
            field=models.CharField(default='', max_length=121),
        ),
        migrations.AddField(
            model_name='gedwra',
            name='samswfwyn',
            field=models.ForeignKey(null=True, related_name='+', to='gtfgy.Rqjyygz'),
        ),
        migrations.DeleteModel(
            name='Vmnilim',
        ),
    ]
