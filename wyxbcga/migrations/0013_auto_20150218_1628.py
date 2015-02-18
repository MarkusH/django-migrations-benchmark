# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rqwywo', '0011_auto_20150218_1628'),
        ('wyxbcga', '0012_auto_20150218_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oblwdacdf',
            name='ohjnftmzh',
        ),
        migrations.RemoveField(
            model_name='rsaiyadejv',
            name='aabsvd',
        ),
        migrations.AddField(
            model_name='oblwdacdf',
            name='eezewl',
            field=models.ForeignKey(null=True, related_name='+', to='rqwywo.Huqprglqp'),
        ),
    ]
