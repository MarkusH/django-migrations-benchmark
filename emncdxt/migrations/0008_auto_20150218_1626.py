# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruvaymw', '0013_auto_20150218_1625'),
        ('emncdxt', '0007_delete_ktiod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shgjep',
            name='ubxdjav',
        ),
        migrations.AddField(
            model_name='shgjep',
            name='lxxaql',
            field=models.OneToOneField(null=True, related_name='+', to='ruvaymw.Hhnwphllci'),
        ),
    ]
