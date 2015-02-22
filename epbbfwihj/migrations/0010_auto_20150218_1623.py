# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epbbfwihj', '0009_apnbivckq_xcnfodzv'),
    ]

    run_before = [
        ('ukxhbn', '0004_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uzdthbetj',
            name='cmzqytyp',
        ),
        migrations.RemoveField(
            model_name='zfpgchkbaz',
            name='yttrt',
        ),
        migrations.AddField(
            model_name='uzdthbetj',
            name='qrawui',
            field=models.CharField(default='', max_length=172),
        ),
    ]
