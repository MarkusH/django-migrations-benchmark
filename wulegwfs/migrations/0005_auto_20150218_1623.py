# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khwbgr', '0006_auto_20150218_1623'),
        ('wulegwfs', '0004_xcasayyn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yxsnty',
            name='qhjcri',
        ),
        migrations.AddField(
            model_name='yxsnty',
            name='orxnuylir',
            field=models.ForeignKey(null=True, related_name='+', to='khwbgr.Bwshcnprcg'),
        ),
    ]
