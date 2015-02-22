# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apbqku', '0005_auto_20150218_1622'),
        ('zxxavsovs', '0004_kiikphbz_tbzky'),
        ('zngxahi', '0005_auto_20150218_1622'),
    ]

    run_before = [
        ('apbqku', '0006_delete_ssgsglh'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bdontoyqti',
            name='nmctlsx',
        ),
        migrations.AddField(
            model_name='bdontoyqti',
            name='wjquqibaq',
            field=models.ForeignKey(null=True, related_name='+', to='zxxavsovs.Fiellmltob'),
        ),
        migrations.AddField(
            model_name='nnkqr',
            name='wcytnskou',
            field=models.ForeignKey(null=True, related_name='+', to='apbqku.Ssgsglh'),
        ),
    ]
