# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohutfvb', '0010_remove_qpuji_pozefnkorz'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sonmvoj',
        ),
        migrations.RemoveField(
            model_name='ecgjvad',
            name='zxnnutgo',
        ),
        migrations.AddField(
            model_name='ecgjvad',
            name='dmlqug',
            field=models.CharField(default='', max_length=96),
        ),
    ]
