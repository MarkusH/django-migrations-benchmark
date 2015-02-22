# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0016_delete_qrwsj'),
        ('digmcd', '0018_auto_20150218_1630'),
    ]

    run_before = [
        ('joavhqi', '0016_auto_20150218_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gtekbplhr',
            name='npzyjho',
        ),
        migrations.AddField(
            model_name='gtekbplhr',
            name='gzbctv',
            field=models.ForeignKey(null=True, related_name='+', to='foijx.Cnkdojs'),
        ),
        migrations.AddField(
            model_name='mqnavvvb',
            name='tffxa',
            field=models.CharField(default='', max_length=157),
        ),
    ]
