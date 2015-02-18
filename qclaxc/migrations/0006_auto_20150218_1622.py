# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irmtbds', '0004_auto_20150218_1622'),
        ('qclaxc', '0005_hlpgeaqix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jvoopceqsv',
            name='icswoha',
        ),
        migrations.AddField(
            model_name='yswziiulyl',
            name='mzpaepi',
            field=models.ForeignKey(null=True, related_name='+', to='irmtbds.Rqikftw'),
        ),
    ]
