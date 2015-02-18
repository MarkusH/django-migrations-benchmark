# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohutfvb', '0012_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qpuji',
            name='saiuw',
        ),
        migrations.AddField(
            model_name='qpuji',
            name='hpnkk',
            field=models.CharField(default='', max_length=51),
        ),
    ]
