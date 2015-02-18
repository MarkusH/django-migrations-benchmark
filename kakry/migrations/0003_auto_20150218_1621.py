# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakry', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aefqhqkmm',
            name='aqpoesk',
        ),
        migrations.RemoveField(
            model_name='mfivvxhds',
            name='dlcolp',
        ),
        migrations.AddField(
            model_name='aefqhqkmm',
            name='ftnkzwba',
            field=models.CharField(default='', max_length=53),
        ),
        migrations.AddField(
            model_name='lmxjryphro',
            name='nlxhwbmf',
            field=models.CharField(default='', max_length=114),
        ),
    ]
