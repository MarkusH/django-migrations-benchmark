# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rqwywo', '0006_auto_20150218_1623'),
        ('gbsaqmaxu', '0007_nwyctrmqpq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vvyni',
            name='wnyycawcq',
        ),
        migrations.AddField(
            model_name='avwudusy',
            name='osqkql',
            field=models.CharField(default='', max_length=103),
        ),
        migrations.AddField(
            model_name='lshmrghvzw',
            name='olicbgstaw',
            field=models.OneToOneField(null=True, related_name='+', to='rqwywo.Gkiwtx'),
        ),
    ]
