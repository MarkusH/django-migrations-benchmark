# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruvaymw', '0019_auto_20150218_1631'),
    ]

    run_before = [
        ('gbsaqmaxu', '0019_delete_vvyni'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fxsiyvw',
            name='bigwfusa',
        ),
        migrations.AddField(
            model_name='wmifd',
            name='tbtrybc',
            field=models.CharField(default='', max_length=191),
        ),
        migrations.DeleteModel(
            name='Fxsiyvw',
        ),
    ]
