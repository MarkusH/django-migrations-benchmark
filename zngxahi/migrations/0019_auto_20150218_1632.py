# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zngxahi', '0018_vnoruiao_mmpdy'),
    ]

    run_before = [
        ('gbsaqmaxu', '0019_delete_vvyni'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kbgdzldxz',
            name='jdhsjo',
        ),
        migrations.RemoveField(
            model_name='qahkfonewx',
            name='ditijdjnl',
        ),
        migrations.RemoveField(
            model_name='rxxpitmckt',
            name='dnzdal',
        ),
        migrations.AddField(
            model_name='rxxpitmckt',
            name='fimfcmg',
            field=models.IntegerField(default=0),
        ),
    ]
