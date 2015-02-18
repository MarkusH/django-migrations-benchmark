# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohutfvb', '0014_auto_20150218_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qpuji',
            name='hpnkk',
        ),
        migrations.AddField(
            model_name='qpuji',
            name='dgyoob',
            field=models.CharField(default='', max_length=155),
        ),
    ]
