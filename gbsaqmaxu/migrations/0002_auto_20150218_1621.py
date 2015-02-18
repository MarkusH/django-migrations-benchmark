# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0001_initial'),
        ('gbsaqmaxu', '0001_initial'),
        ('ysgxuyu', '0001_initial'),
        ('cohutfvb', '0002_livljpedso_xfxzoezgv'),
        ('digmcd', '0002_xovte_fhgkhncfld'),
        ('rqwywo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zdahw',
            name='binimm',
            field=models.ForeignKey(null=True, related_name='+', to='rqwywo.Lxcurbmhu'),
        ),
        migrations.AddField(
            model_name='rbodr',
            name='hmigi',
            field=models.ForeignKey(null=True, related_name='+', to='ysgxuyu.Omtmse'),
        ),
        migrations.AddField(
            model_name='nhlpe',
            name='wfetmax',
            field=models.ForeignKey(null=True, related_name='+', to='cohutfvb.Sonmvoj'),
        ),
        migrations.AddField(
            model_name='lshmrghvzw',
            name='iqdetwvwf',
            field=models.OneToOneField(null=True, related_name='+', to='zhavbmq.Rhhbgxx'),
        ),
        migrations.AddField(
            model_name='knqau',
            name='lctemiulg',
            field=models.OneToOneField(null=True, related_name='+', to='digmcd.Untgafvod'),
        ),
    ]
