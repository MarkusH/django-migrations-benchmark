# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rqwywo', '0005_remove_huqprglqp_lknuczrw'),
        ('zavygg', '0006_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oqyncxevyj',
            name='lykvcrgp',
        ),
        migrations.AddField(
            model_name='jydvnf',
            name='caohod',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='oqyncxevyj',
            name='cqpevou',
            field=models.OneToOneField(null=True, related_name='+', to='rqwywo.Xaszfxobvf'),
        ),
    ]
