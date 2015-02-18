# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irmtbds', '0002_auto_20150218_1621'),
        ('joavhqi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iowgy',
            name='kffkvcz',
        ),
        migrations.AddField(
            model_name='iowgy',
            name='rcmqduvnsb',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='uodtjnez',
            name='dpnzgpxom',
            field=models.OneToOneField(null=True, related_name='+', to='irmtbds.Rqzheruyb'),
        ),
    ]
