# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakry', '0003_auto_20150218_1621'),
        ('adlorvp', '0005_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bauxko',
            name='wlkthj',
        ),
        migrations.AddField(
            model_name='bauxko',
            name='mjgvx',
            field=models.ForeignKey(null=True, related_name='+', to='kakry.Xgsseizbpr'),
        ),
    ]
