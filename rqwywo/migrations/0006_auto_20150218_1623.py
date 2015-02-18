# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcfrcnas', '0010_auto_20150218_1623'),
        ('rqwywo', '0005_remove_huqprglqp_lknuczrw'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lxcurbmhu',
            name='oncyszdy',
        ),
        migrations.RemoveField(
            model_name='xaszfxobvf',
            name='syoyminf',
        ),
        migrations.AddField(
            model_name='lxcurbmhu',
            name='ecotjsdibe',
            field=models.OneToOneField(null=True, related_name='+', to='ftcfrcnas.Cukzic'),
        ),
        migrations.AddField(
            model_name='xaszfxobvf',
            name='iamarlmq',
            field=models.CharField(default='', max_length=124),
        ),
    ]
