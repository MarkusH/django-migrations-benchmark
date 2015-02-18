# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zxxavsovs', '0009_auto_20150218_1626'),
        ('cuspknbh', '0013_auto_20150218_1626'),
        ('mjdxvqk', '0012_auto_20150218_1625'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ehopcsp',
        ),
        migrations.RemoveField(
            model_name='edugsywcj',
            name='piqojyx',
        ),
        migrations.AddField(
            model_name='edugsywcj',
            name='oseje',
            field=models.OneToOneField(null=True, related_name='+', to='zxxavsovs.Fiellmltob'),
        ),
        migrations.AddField(
            model_name='xglneni',
            name='ltnmc',
            field=models.OneToOneField(null=True, related_name='+', to='cuspknbh.Djbbtxk'),
        ),
    ]
