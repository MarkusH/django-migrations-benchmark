# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burhjvc', '0002_auto_20150218_1621'),
        ('rqwywo', '0001_initial'),
        ('zavygg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdzdhpq',
            name='bwexzs',
            field=models.OneToOneField(null=True, related_name='+', to='rqwywo.Gkiwtx'),
        ),
        migrations.AddField(
            model_name='aziftfctf',
            name='fhxldzom',
            field=models.ForeignKey(null=True, related_name='+', to='zavygg.Jydvnf'),
        ),
    ]
