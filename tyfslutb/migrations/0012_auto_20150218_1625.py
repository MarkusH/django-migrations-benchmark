# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyfslutb', '0011_rfdhb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvzmphnk',
            name='bcxikdtwa',
        ),
        migrations.RemoveField(
            model_name='copkdxcnlp',
            name='gczeinwy',
        ),
        migrations.RemoveField(
            model_name='ixmfsgch',
            name='zovmenwqiy',
        ),
        migrations.AddField(
            model_name='copkdxcnlp',
            name='fejjfwfzs',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='ixmfsgch',
            name='lwczoav',
            field=models.CharField(default='', max_length=129),
        ),
        migrations.DeleteModel(
            name='Cvzmphnk',
        ),
    ]
