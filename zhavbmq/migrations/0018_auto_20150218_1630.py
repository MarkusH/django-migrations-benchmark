# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0017_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bdniaupe',
            name='nftecr',
        ),
        migrations.AddField(
            model_name='bdniaupe',
            name='plcox',
            field=models.CharField(default='', max_length=53),
        ),
        migrations.AddField(
            model_name='vzhhl',
            name='odnpyo',
            field=models.CharField(default='', max_length=60),
        ),
    ]
