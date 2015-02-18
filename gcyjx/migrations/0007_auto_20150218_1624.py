# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcyjx', '0006_nmbztrlh'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nmbztrlh',
            name='widhow',
        ),
        migrations.AddField(
            model_name='nmbztrlh',
            name='xmyjydanpz',
            field=models.IntegerField(default=0),
        ),
    ]
