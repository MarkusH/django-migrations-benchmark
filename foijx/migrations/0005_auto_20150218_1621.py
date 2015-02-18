# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rwlfplwktj', '0002_knoeepjnhs_kluyzayvh'),
        ('foijx', '0004_auto_20150218_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='abmhnczd',
            name='hekwccfc',
            field=models.OneToOneField(null=True, related_name='+', to='rwlfplwktj.Knoeepjnhs'),
        ),
        migrations.AddField(
            model_name='gsdqrijpp',
            name='mzmegwgymf',
            field=models.IntegerField(default=0),
        ),
    ]
