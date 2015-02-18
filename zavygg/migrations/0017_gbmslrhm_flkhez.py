# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khwbgr', '0010_auto_20150218_1632'),
        ('zavygg', '0016_auto_20150218_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='gbmslrhm',
            name='flkhez',
            field=models.ForeignKey(null=True, related_name='+', to='khwbgr.Ibuazau'),
        ),
    ]
