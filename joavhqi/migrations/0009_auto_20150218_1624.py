# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joavhqi', '0008_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nizqeesp',
            name='qmhtlk',
        ),
        migrations.RemoveField(
            model_name='rdhhdq',
            name='yhhsrszrp',
        ),
        migrations.AddField(
            model_name='rdhhdq',
            name='xxngkrby',
            field=models.CharField(default='', max_length=248),
        ),
    ]
