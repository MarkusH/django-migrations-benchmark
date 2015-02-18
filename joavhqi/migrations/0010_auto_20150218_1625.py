# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qqpppzas', '0009_auto_20150218_1624'),
        ('joavhqi', '0009_auto_20150218_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pqetbg',
            name='vjyxkovspd',
        ),
        migrations.RemoveField(
            model_name='yusanbjmh',
            name='jskimt',
        ),
        migrations.AddField(
            model_name='pqetbg',
            name='jhildfk',
            field=models.OneToOneField(null=True, related_name='+', to='qqpppzas.Jchddfi'),
        ),
    ]
