# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digmcd', '0007_auto_20150218_1622'),
        ('tyfslutb', '0004_auto_20150218_1621'),
    ]

    run_before = [
        ('digmcd', '0011_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvzmphnk',
            name='xhcatgbtsw',
        ),
        migrations.RemoveField(
            model_name='qcwbo',
            name='yuafmza',
        ),
        migrations.RemoveField(
            model_name='ynbpgqn',
            name='oepaepmp',
        ),
        migrations.AddField(
            model_name='cvzmphnk',
            name='udzzqrxgk',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qcwbo',
            name='dokqdbprt',
            field=models.OneToOneField(null=True, related_name='+', to='digmcd.Arqcdv'),
        ),
    ]
