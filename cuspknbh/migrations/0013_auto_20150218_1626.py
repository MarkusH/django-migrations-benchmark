# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuspknbh', '0012_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='djbbtxk',
            name='szwaxyb',
        ),
        migrations.AddField(
            model_name='djbbtxk',
            name='nafoj',
            field=models.IntegerField(default=0),
        ),
    ]
