# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uivaguf', '0013_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zwjgfcdi',
            name='ymtyj',
        ),
        migrations.AddField(
            model_name='zwjgfcdi',
            name='cudmzwxi',
            field=models.CharField(default='', max_length=125),
        ),
    ]
