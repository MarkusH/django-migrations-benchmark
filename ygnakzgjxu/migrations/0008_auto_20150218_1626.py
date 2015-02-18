# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygnakzgjxu', '0007_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ttzean',
            name='zosoxtv',
        ),
        migrations.RemoveField(
            model_name='xdwhlpqgw',
            name='potlucvgl',
        ),
        migrations.AddField(
            model_name='xdwhlpqgw',
            name='qzrfs',
            field=models.CharField(default='', max_length=97),
        ),
        migrations.DeleteModel(
            name='Ttzean',
        ),
    ]
