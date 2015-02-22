# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khwbgr', '0001_initial'),
        ('adlorvp', '0002_kzrfnfxko_rfezjxndz'),
    ]

    run_before = [
        ('khwbgr', '0004_auto_20150218_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='kmygwyorsi',
            name='shkjv',
            field=models.OneToOneField(null=True, related_name='+', to='khwbgr.Qsqcspjrgx'),
        ),
    ]
