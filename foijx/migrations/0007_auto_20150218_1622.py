# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0006_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abmhnczd',
            name='hekwccfc',
        ),
        migrations.AddField(
            model_name='cnkdojs',
            name='sgtwhfdeig',
            field=models.CharField(default='', max_length=170),
        ),
        migrations.AddField(
            model_name='wrafoshzom',
            name='iatgcl',
            field=models.IntegerField(default=0),
        ),
    ]
