# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0010_auto_20150218_1623'),
    ]

    run_before = [
        ('pnxyvqx', '0012_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dvkdj',
            name='gsscvcgrm',
        ),
        migrations.DeleteModel(
            name='Dvkdj',
        ),
    ]
