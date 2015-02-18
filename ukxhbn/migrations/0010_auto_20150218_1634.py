# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rqwywo', '0016_auto_20150218_1634'),
        ('ukxhbn', '0009_auto_20150218_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aciaff',
            name='atqvcg',
        ),
        migrations.AddField(
            model_name='aciaff',
            name='dztjqxsufg',
            field=models.ForeignKey(null=True, related_name='+', to='rqwywo.Trhinrdlr'),
        ),
    ]
