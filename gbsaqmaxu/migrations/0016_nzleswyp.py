# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joavhqi', '0013_auto_20150218_1628'),
        ('gbsaqmaxu', '0015_nhlpe_afpyhakre'),
    ]

    run_before = [
        ('joavhqi', '0016_auto_20150218_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nzleswyp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cfvih', models.OneToOneField(null=True, related_name='+', to='joavhqi.Uodtjnez')),
            ],
        ),
    ]
