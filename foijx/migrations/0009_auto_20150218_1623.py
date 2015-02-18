# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0008_auto_20150218_1623'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mvmwqukrbx',
        ),
        migrations.RemoveField(
            model_name='gsdqrijpp',
            name='mzmegwgymf',
        ),
        migrations.AddField(
            model_name='gsdqrijpp',
            name='sagzj',
            field=models.IntegerField(default=0),
        ),
    ]
