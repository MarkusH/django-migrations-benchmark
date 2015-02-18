# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esznwrr', '0004_delete_vppjpa'),
        ('qqpppzas', '0009_auto_20150218_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xcuutwsyfn',
            name='asyjcrv',
        ),
        migrations.AddField(
            model_name='igtbspg',
            name='fpakgnfxli',
            field=models.ForeignKey(null=True, related_name='+', to='esznwrr.Cepov'),
        ),
        migrations.AddField(
            model_name='mukbde',
            name='vdpfetqazw',
            field=models.CharField(default='', max_length=113),
        ),
        migrations.AddField(
            model_name='xcuutwsyfn',
            name='hcidp',
            field=models.IntegerField(default=0),
        ),
    ]
