# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joavhqi', '0011_yusanbjmh_onkbpnnv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pqetbg',
            name='jhildfk',
        ),
        migrations.RemoveField(
            model_name='lfssmpr',
            name='qweppfqt',
        ),
        migrations.AddField(
            model_name='lfssmpr',
            name='xlfkpk',
            field=models.CharField(default='', max_length=52),
        ),
        migrations.DeleteModel(
            name='Pqetbg',
        ),
    ]
