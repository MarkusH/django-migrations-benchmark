# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavygg', '0005_auto_20150218_1622'),
        ('burhjvc', '0007_auto_20150218_1622'),
        ('foijx', '0005_auto_20150218_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='gsdqrijpp',
            name='akszwqxbr',
            field=models.ForeignKey(null=True, related_name='+', to='zavygg.Ligxr'),
        ),
        migrations.AddField(
            model_name='qrwsj',
            name='zdvvjpppsi',
            field=models.OneToOneField(null=True, related_name='+', to='burhjvc.Ydprem'),
        ),
    ]
