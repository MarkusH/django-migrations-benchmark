# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ukxhbn', '0006_qujmudiaaa'),
        ('qclaxc', '0010_auto_20150218_1625'),
    ]

    run_before = [
        ('ladqux', '0006_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hlpgeaqix',
            name='nrrdexkvmq',
        ),
        migrations.RemoveField(
            model_name='ladoumxyr',
            name='rophhewd',
        ),
        migrations.AddField(
            model_name='hlpgeaqix',
            name='xrfgwsb',
            field=models.ForeignKey(null=True, related_name='+', to='ukxhbn.Qujmudiaaa'),
        ),
    ]
