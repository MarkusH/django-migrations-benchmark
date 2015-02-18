# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yiupu', '0004_auto_20150218_1623'),
        ('cmsrp', '0003_ncysy_lkvgwwfoan'),
        ('tyfslutb', '0009_auto_20150218_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='ihswfvupi',
            name='fmuxala',
            field=models.ForeignKey(null=True, related_name='+', to='yiupu.Zzsheqzf'),
        ),
        migrations.AddField(
            model_name='qcwbo',
            name='nevqtm',
            field=models.ForeignKey(null=True, related_name='+', to='cmsrp.Cpmqvzn'),
        ),
    ]
