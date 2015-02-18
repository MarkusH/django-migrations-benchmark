# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wulegwfs', '0005_auto_20150218_1623'),
        ('avwpufexob', '0009_aunuwoo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fvlkcjd',
            name='onlvfzdsk',
        ),
        migrations.AddField(
            model_name='fvlkcjd',
            name='psxjvm',
            field=models.ForeignKey(null=True, related_name='+', to='wulegwfs.Xcasayyn'),
        ),
    ]
