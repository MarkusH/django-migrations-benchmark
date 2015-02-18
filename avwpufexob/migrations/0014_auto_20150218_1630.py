# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avwpufexob', '0013_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nhpkrhkql',
            name='gphdl',
        ),
        migrations.AddField(
            model_name='aunuwoo',
            name='qmkmtxr',
            field=models.CharField(default='', max_length=141),
        ),
        migrations.AddField(
            model_name='nhpkrhkql',
            name='qilej',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='yejdqycpmg',
            name='grygcsjy',
            field=models.CharField(default='', max_length=254),
        ),
    ]
