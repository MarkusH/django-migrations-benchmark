# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joavhqi', '0009_auto_20150218_1624'),
        ('digmcd', '0013_remove_zaganduq_plaqa'),
    ]

    run_before = [
        ('esznwrr', '0004_delete_vppjpa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gxovs',
            name='ovvkibpppv',
        ),
        migrations.RemoveField(
            model_name='gtekbplhr',
            name='pdxvfhs',
        ),
        migrations.RemoveField(
            model_name='lemzs',
            name='jaozjpsixx',
        ),
        migrations.RemoveField(
            model_name='rdfrrg',
            name='yayujeww',
        ),
        migrations.RemoveField(
            model_name='zyjgcrtsvt',
            name='mszzimuh',
        ),
        migrations.AddField(
            model_name='gtekbplhr',
            name='npzyjho',
            field=models.ForeignKey(null=True, related_name='+', to='joavhqi.Uodtjnez'),
        ),
        migrations.DeleteModel(
            name='Gxovs',
        ),
    ]
