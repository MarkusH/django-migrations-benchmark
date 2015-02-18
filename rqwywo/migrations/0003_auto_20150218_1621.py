# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtfgy', '0006_auto_20150218_1621'),
        ('rqwywo', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='huqprglqp',
            name='xumeqhx',
        ),
        migrations.RemoveField(
            model_name='uxpep',
            name='wognfx',
        ),
        migrations.RemoveField(
            model_name='xaszfxobvf',
            name='iskdepqo',
        ),
        migrations.AddField(
            model_name='huqprglqp',
            name='lknuczrw',
            field=models.ForeignKey(null=True, related_name='+', to='gtfgy.Wnhvelxdeb'),
        ),
    ]
