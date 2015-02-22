# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gbsaqmaxu', '0013_auto_20150218_1626'),
        ('foijx', '0012_auto_20150218_1626'),
        ('zngxahi', '0012_auto_20150218_1625'),
    ]

    run_before = [
        ('qqpppzas', '0012_auto_20150218_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vnoruiao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtrfnedgq', models.OneToOneField(null=True, related_name='+', to='foijx.Cnkdojs')),
            ],
        ),
        migrations.RemoveField(
            model_name='eauslyif',
            name='ryfajv',
        ),
        migrations.RemoveField(
            model_name='llnksobygh',
            name='mfhovgyh',
        ),
        migrations.AddField(
            model_name='kbgdzldxz',
            name='anphrsovlr',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='llnksobygh',
            name='ewoyglmblj',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qahkfonewx',
            name='ditijdjnl',
            field=models.OneToOneField(null=True, related_name='+', to='gbsaqmaxu.Vvyni'),
        ),
    ]
