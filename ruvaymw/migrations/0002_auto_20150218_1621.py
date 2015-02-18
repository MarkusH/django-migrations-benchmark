# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kfapsax', '0001_initial'),
        ('ruvaymw', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owamswc',
            name='ekqpnk',
        ),
        migrations.RemoveField(
            model_name='wmifd',
            name='ctfflurp',
        ),
        migrations.AddField(
            model_name='owamswc',
            name='iijffzuw',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wmifd',
            name='yalhscl',
            field=models.OneToOneField(null=True, related_name='+', to='kfapsax.Sehvi'),
        ),
    ]
