# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtfgy', '0015_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rqjyygz',
            name='syyrsnfru',
        ),
        migrations.AddField(
            model_name='rqjyygz',
            name='dxqngyccu',
            field=models.CharField(default='', max_length=20),
        ),
    ]
