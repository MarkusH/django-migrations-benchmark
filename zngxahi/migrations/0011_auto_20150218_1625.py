# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zxxavsovs', '0008_auto_20150218_1625'),
        ('zngxahi', '0010_hiqedajgiu_yfdbtklxb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qahkfonewx',
            name='gwrlr',
        ),
        migrations.AddField(
            model_name='qahkfonewx',
            name='eckmsf',
            field=models.ForeignKey(null=True, related_name='+', to='zxxavsovs.Yjuyutcqq'),
        ),
    ]
