# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uivaguf', '0016_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zwjgfcdi',
            name='cudmzwxi',
        ),
        migrations.AddField(
            model_name='zwjgfcdi',
            name='crkhxew',
            field=models.CharField(default='', max_length=11),
        ),
    ]
