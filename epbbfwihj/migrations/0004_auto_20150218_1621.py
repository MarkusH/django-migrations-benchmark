# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epbbfwihj', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gejrsf',
            name='wnttrpau',
        ),
        migrations.RemoveField(
            model_name='pbnaktpzhs',
            name='ixryziwdzn',
        ),
        migrations.AddField(
            model_name='gejrsf',
            name='hjtbpctd',
            field=models.CharField(default='', max_length=209),
        ),
    ]
