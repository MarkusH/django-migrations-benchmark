# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruvaymw', '0008_auto_20150218_1623'),
        ('kakry', '0007_delete_aivqb'),
    ]

    operations = [
        migrations.AddField(
            model_name='flfbdpu',
            name='jtwrql',
            field=models.CharField(default='', max_length=104),
        ),
        migrations.AddField(
            model_name='lmxjryphro',
            name='qsochd',
            field=models.ForeignKey(null=True, related_name='+', to='ruvaymw.Wmifd'),
        ),
        migrations.AddField(
            model_name='xgsseizbpr',
            name='fvqktro',
            field=models.CharField(default='', max_length=141),
        ),
    ]
