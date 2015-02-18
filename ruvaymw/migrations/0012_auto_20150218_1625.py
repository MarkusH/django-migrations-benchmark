# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ukxhbn', '0005_auto_20150218_1624'),
        ('ruvaymw', '0011_delete_owamswc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ndhcup',
            name='kvekefr',
        ),
        migrations.RemoveField(
            model_name='wmifd',
            name='ztdwwxnoeo',
        ),
        migrations.AddField(
            model_name='hkbvwjilj',
            name='ryflyqqcrw',
            field=models.OneToOneField(null=True, related_name='+', to='ukxhbn.Ikuwr'),
        ),
    ]
