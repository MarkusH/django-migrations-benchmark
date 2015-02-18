# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digmcd', '0009_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rdfrrg',
            name='lihyfbg',
        ),
        migrations.AddField(
            model_name='untgafvod',
            name='matfqq',
            field=models.CharField(default='', max_length=175),
        ),
        migrations.AddField(
            model_name='yymzlvsz',
            name='cjumbggroa',
            field=models.CharField(default='', max_length=181),
        ),
    ]
