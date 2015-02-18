# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyxbcga', '0001_initial'),
        ('pkfudme', '0001_initial'),
        ('foijx', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='hcblxrqme',
            name='ztqdo',
            field=models.ForeignKey(null=True, related_name='+', to='wyxbcga.Eezxvbbvmn'),
        ),
        migrations.AddField(
            model_name='ewxxluebq',
            name='sqyiv',
            field=models.ForeignKey(null=True, related_name='+', to='wyxbcga.Rsaiyadejv'),
        ),
        migrations.AddField(
            model_name='dbpile',
            name='yamkggnk',
            field=models.OneToOneField(null=True, related_name='+', to='foijx.Qrwsj'),
        ),
    ]
