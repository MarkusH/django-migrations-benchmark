# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnxyvqx', '0011_ecatm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nrnexasxp',
            name='irgwicvs',
        ),
        migrations.RemoveField(
            model_name='aehywz',
            name='yehjk',
        ),
        migrations.RemoveField(
            model_name='nenfvguk',
            name='yglmn',
        ),
        migrations.AddField(
            model_name='aehywz',
            name='znmxhx',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Nrnexasxp',
        ),
    ]
