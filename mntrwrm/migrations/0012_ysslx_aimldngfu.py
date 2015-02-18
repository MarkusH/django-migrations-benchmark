# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mntrwrm', '0011_auto_20150218_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='ysslx',
            name='aimldngfu',
            field=models.CharField(default='', max_length=241),
        ),
    ]
