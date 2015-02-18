# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcfrcnas', '0005_qibygpddzw_nzlzvpdg'),
        ('digmcd', '0005_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zyjgcrtsvt',
            name='tdwxs',
        ),
        migrations.AddField(
            model_name='rdfrrg',
            name='anylxapd',
            field=models.ForeignKey(null=True, related_name='+', to='ftcfrcnas.Lqfdippdc'),
        ),
        migrations.AddField(
            model_name='zyjgcrtsvt',
            name='mszzimuh',
            field=models.IntegerField(default=0),
        ),
    ]
