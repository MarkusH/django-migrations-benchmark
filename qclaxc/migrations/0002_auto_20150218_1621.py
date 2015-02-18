# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ladqux', '0001_initial'),
        ('kfapsax', '0001_initial'),
        ('zhavbmq', '0001_initial'),
        ('tyfslutb', '0001_initial'),
        ('qclaxc', '0001_initial'),
        ('ukxhbn', '0001_initial'),
        ('geemkrwi', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='rmtucrztaq',
            name='heducuype',
            field=models.OneToOneField(null=True, related_name='+', to='zhavbmq.Bdniaupe'),
        ),
        migrations.AddField(
            model_name='qindcumiy',
            name='rwtwpy',
            field=models.ForeignKey(null=True, related_name='+', to='tyfslutb.Qhzppcqwku'),
        ),
        migrations.AddField(
            model_name='pmcbxoetr',
            name='npfpduxdlb',
            field=models.ForeignKey(null=True, related_name='+', to='ukxhbn.Dcphul'),
        ),
        migrations.AddField(
            model_name='ooecads',
            name='nflopwecc',
            field=models.ForeignKey(null=True, related_name='+', to='kfapsax.Kmwzcb'),
        ),
        migrations.AddField(
            model_name='ladoumxyr',
            name='rophhewd',
            field=models.ForeignKey(null=True, related_name='+', to='ladqux.Yxjjlex'),
        ),
        migrations.AddField(
            model_name='jvoopceqsv',
            name='icswoha',
            field=models.OneToOneField(null=True, related_name='+', to='geemkrwi.Meymafbbi'),
        ),
    ]
