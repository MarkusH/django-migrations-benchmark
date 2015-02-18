# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ladqux', '0003_auto_20150218_1622'),
        ('qqpppzas', '0004_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vdscpy',
            name='mxjhvnbbqm',
        ),
        migrations.RemoveField(
            model_name='xcuutwsyfn',
            name='bwpigha',
        ),
        migrations.AddField(
            model_name='prljmjou',
            name='hiacissed',
            field=models.OneToOneField(null=True, related_name='+', to='ladqux.Yxjjlex'),
        ),
        migrations.AddField(
            model_name='xcuutwsyfn',
            name='kykqcsvbz',
            field=models.CharField(default='', max_length=152),
        ),
    ]
