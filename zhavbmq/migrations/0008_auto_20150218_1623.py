# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0007_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dvkdj',
            name='jzwapass',
        ),
        migrations.RemoveField(
            model_name='gwmyxcxdii',
            name='lnioihvte',
        ),
        migrations.RemoveField(
            model_name='ulvookvun',
            name='tugjdleqdq',
        ),
        migrations.AddField(
            model_name='gwmyxcxdii',
            name='mhcua',
            field=models.IntegerField(default=0),
        ),
    ]
