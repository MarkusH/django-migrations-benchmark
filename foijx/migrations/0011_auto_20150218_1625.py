# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0010_auto_20150218_1624'),
    ]

    run_before = [
        ('pnxyvqx', '0012_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cnkdojs',
            name='adedvcyxhq',
        ),
        migrations.RemoveField(
            model_name='qqktwujdfq',
            name='drdrumut',
        ),
        migrations.RemoveField(
            model_name='qrwsj',
            name='holofste',
        ),
        migrations.AddField(
            model_name='cnkdojs',
            name='hetxikomrw',
            field=models.CharField(default='', max_length=200),
        ),
    ]
