# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glcmkwkzv', '0008_delete_lowamdo'),
    ]

    run_before = [
        ('zavygg', '0011_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idmamodyjp',
            name='mibgfhq',
        ),
        migrations.RemoveField(
            model_name='unnork',
            name='wvljmakxy',
        ),
        migrations.AddField(
            model_name='idmamodyjp',
            name='vmxnec',
            field=models.IntegerField(default=0),
        ),
    ]
