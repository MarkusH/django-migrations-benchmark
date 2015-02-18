# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rwlfplwktj', '0002_knoeepjnhs_kluyzayvh'),
        ('uivaguf', '0004_ubuhm_bzhgokn'),
        ('avwpufexob', '0005_auto_20150218_1621'),
        ('tyfslutb', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qcwbo',
            name='zxzurr',
        ),
        migrations.RemoveField(
            model_name='ynbpgqn',
            name='dpwwwnuj',
        ),
        migrations.AddField(
            model_name='djnppzsr',
            name='dkptlqocjt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='juemb',
            name='ldineuo',
            field=models.ForeignKey(null=True, related_name='+', to='uivaguf.Onmti'),
        ),
        migrations.AddField(
            model_name='qcwbo',
            name='yuafmza',
            field=models.OneToOneField(null=True, related_name='+', to='rwlfplwktj.Knoeepjnhs'),
        ),
        migrations.AddField(
            model_name='ynbpgqn',
            name='oepaepmp',
            field=models.OneToOneField(null=True, related_name='+', to='avwpufexob.Ubpmj'),
        ),
    ]
