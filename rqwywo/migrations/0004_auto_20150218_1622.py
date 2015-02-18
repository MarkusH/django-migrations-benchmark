# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zsskgviadw', '0003_auto_20150218_1621'),
        ('qclaxc', '0005_hlpgeaqix'),
        ('rqwywo', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='huqprglqp',
            name='nnibv',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='uxpep',
            name='orgsmbx',
            field=models.ForeignKey(null=True, related_name='+', to='zsskgviadw.Hcetattb'),
        ),
        migrations.AddField(
            model_name='xaszfxobvf',
            name='syoyminf',
            field=models.OneToOneField(null=True, related_name='+', to='qclaxc.Jvoopceqsv'),
        ),
    ]
