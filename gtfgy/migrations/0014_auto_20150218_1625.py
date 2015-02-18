# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irmtbds', '0006_rqikftw_xqmakus'),
        ('tyfslutb', '0013_remove_ynbpgqn_ninzjz'),
        ('gtfgy', '0013_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symqs',
            name='zdbraaw',
        ),
        migrations.AddField(
            model_name='ftwph',
            name='thrfoimmzd',
            field=models.ForeignKey(null=True, related_name='+', to='tyfslutb.Qhzppcqwku'),
        ),
        migrations.AddField(
            model_name='symqs',
            name='cdcocpyto',
            field=models.ForeignKey(null=True, related_name='+', to='irmtbds.Rqikftw'),
        ),
        migrations.AddField(
            model_name='yrekcfrkl',
            name='gvytprt',
            field=models.IntegerField(default=0),
        ),
    ]
