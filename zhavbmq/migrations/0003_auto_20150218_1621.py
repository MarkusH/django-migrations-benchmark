# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakry', '0004_mfivvxhds_erclh'),
        ('zhavbmq', '0002_ulvookvun_zbrqsverm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yqtbfv',
            name='dvtoxrtyw',
        ),
        migrations.AddField(
            model_name='bdniaupe',
            name='swdbw',
            field=models.ForeignKey(null=True, related_name='+', to='kakry.Kiurw'),
        ),
        migrations.AddField(
            model_name='yqtbfv',
            name='huxxsunnjz',
            field=models.IntegerField(default=0),
        ),
    ]
