# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bniworfy', '0016_auto_20150218_1631'),
        ('ygnakzgjxu', '0008_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xdwhlpqgw',
            name='qzrfs',
        ),
        migrations.AddField(
            model_name='xdwhlpqgw',
            name='rwnpcg',
            field=models.ForeignKey(null=True, related_name='+', to='bniworfy.Dvqne'),
        ),
    ]
