# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khwbgr', '0008_auto_20150218_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ibuazau',
            name='qygkfxppc',
        ),
        migrations.AddField(
            model_name='ibuazau',
            name='edfxe',
            field=models.CharField(default='', max_length=141),
        ),
    ]
