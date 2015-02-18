# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnxyvqx', '0008_auto_20150218_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='fmrensoxi',
            name='gserouu',
            field=models.IntegerField(default=0),
        ),
    ]
