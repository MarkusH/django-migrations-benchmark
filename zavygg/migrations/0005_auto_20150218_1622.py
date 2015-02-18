# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavygg', '0004_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ssalb',
            name='eelqndo',
        ),
        migrations.RemoveField(
            model_name='kihvqrmtr',
            name='llmloxxmss',
        ),
        migrations.AddField(
            model_name='kihvqrmtr',
            name='zvauzxvz',
            field=models.CharField(default='', max_length=238),
        ),
        migrations.DeleteModel(
            name='Ssalb',
        ),
    ]
