# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mntrwrm', '0002_xevahddk'),
        ('qclaxc', '0005_hlpgeaqix'),
        ('ruvaymw', '0004_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bdpibttuxi',
            name='zewgqkdoee',
        ),
        migrations.RemoveField(
            model_name='ndhcup',
            name='tqkbptpb',
        ),
        migrations.AddField(
            model_name='bdpibttuxi',
            name='rujqidvzsd',
            field=models.OneToOneField(null=True, related_name='+', to='mntrwrm.Rbhubw'),
        ),
        migrations.AddField(
            model_name='ndhcup',
            name='udvzu',
            field=models.ForeignKey(null=True, related_name='+', to='qclaxc.Jvoopceqsv'),
        ),
    ]
