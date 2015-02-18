# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joavhqi', '0014_sabdmpl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lfssmpr',
            name='xlfkpk',
        ),
        migrations.RemoveField(
            model_name='nizqeesp',
            name='qdmedf',
        ),
        migrations.AddField(
            model_name='lfssmpr',
            name='rxrepc',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='rdhhdq',
            name='fxgfl',
            field=models.IntegerField(default=0),
        ),
    ]
