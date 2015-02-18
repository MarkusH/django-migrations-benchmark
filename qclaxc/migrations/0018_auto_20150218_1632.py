# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qclaxc', '0017_auto_20150218_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yswziiulyl',
            name='omsizc',
        ),
        migrations.AddField(
            model_name='yswziiulyl',
            name='frtrjxbaxz',
            field=models.OneToOneField(null=True, related_name='+', to='qclaxc.Yswziiulyl'),
        ),
    ]
