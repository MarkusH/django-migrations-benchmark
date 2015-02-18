# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etnevwmkj', '0011_mbkkuilliw_cyqufojbwa'),
        ('gbsaqmaxu', '0017_remove_nhlpe_afpyhakre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nwyctrmqpq',
            name='agxtlimu',
        ),
        migrations.RemoveField(
            model_name='nhlpe',
            name='vcwskrliy',
        ),
        migrations.RemoveField(
            model_name='rkmtigdh',
            name='yowznhii',
        ),
        migrations.AddField(
            model_name='rkmtigdh',
            name='egjvljafhq',
            field=models.ForeignKey(null=True, related_name='+', to='etnevwmkj.Wpkevitz'),
        ),
        migrations.DeleteModel(
            name='Nwyctrmqpq',
        ),
    ]
