# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0012_auto_20150218_1626'),
        ('pkfudme', '0009_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mnvmeraq',
            name='qmpes',
        ),
        migrations.AddField(
            model_name='mnvmeraq',
            name='uxahumnfu',
            field=models.OneToOneField(null=True, related_name='+', to='foijx.Flwuyjdlel'),
        ),
    ]
