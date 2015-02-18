# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrmdjc', '0002_guhhjm_ixxlcmb'),
        ('emncdxt', '0003_mioxdvg_uobgln'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shgjep',
            name='hlamaptyhd',
        ),
        migrations.AddField(
            model_name='shgjep',
            name='ubxdjav',
            field=models.OneToOneField(null=True, related_name='+', to='rrmdjc.Gxoqulk'),
        ),
    ]
