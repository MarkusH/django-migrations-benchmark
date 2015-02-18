# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0007_auto_20150218_1622'),
        ('gtfgy', '0007_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rqjyygz',
            name='phklt',
        ),
        migrations.AddField(
            model_name='xlaxaa',
            name='wlgetunnt',
            field=models.OneToOneField(null=True, related_name='+', to='foijx.Abmhnczd'),
        ),
    ]
