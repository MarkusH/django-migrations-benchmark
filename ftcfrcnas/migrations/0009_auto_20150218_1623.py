# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcfrcnas', '0008_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cdardz',
            name='wdjjcbyo',
        ),
        migrations.RemoveField(
            model_name='wjxepwd',
            name='jxowe',
        ),
        migrations.AddField(
            model_name='cdardz',
            name='emduh',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wjxepwd',
            name='grpthucwr',
            field=models.IntegerField(default=0),
        ),
    ]
