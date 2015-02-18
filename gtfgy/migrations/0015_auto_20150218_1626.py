# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zxxavsovs', '0009_auto_20150218_1626'),
        ('mjdxvqk', '0013_auto_20150218_1626'),
        ('gtfgy', '0014_auto_20150218_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='symqs',
            name='cuean',
            field=models.ForeignKey(null=True, related_name='+', to='zxxavsovs.Aeaoqky'),
        ),
        migrations.AddField(
            model_name='wnhvelxdeb',
            name='zhuhn',
            field=models.OneToOneField(null=True, related_name='+', to='mjdxvqk.Unnnbu'),
        ),
        migrations.AddField(
            model_name='xlaxaa',
            name='jihubfhawn',
            field=models.IntegerField(default=0),
        ),
    ]
