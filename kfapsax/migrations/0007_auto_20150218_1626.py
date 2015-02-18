# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emncdxt', '0008_auto_20150218_1626'),
        ('kfapsax', '0006_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sehvi',
            name='ywngrzbcq',
        ),
        migrations.AddField(
            model_name='sehvi',
            name='zjrwgrgp',
            field=models.OneToOneField(null=True, related_name='+', to='emncdxt.Mioxdvg'),
        ),
    ]
