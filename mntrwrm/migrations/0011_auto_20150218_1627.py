# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mntrwrm', '0010_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xevahddk',
            name='vxckqc',
        ),
        migrations.AddField(
            model_name='xevahddk',
            name='unyyz',
            field=models.IntegerField(default=0),
        ),
    ]
