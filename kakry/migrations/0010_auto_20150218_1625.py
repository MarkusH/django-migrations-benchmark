# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcyjx', '0008_auto_20150218_1625'),
        ('kakry', '0009_remove_ajbkovws_kmhhp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aefqhqkmm',
            name='ftnkzwba',
        ),
        migrations.AddField(
            model_name='aefqhqkmm',
            name='yupnznks',
            field=models.OneToOneField(null=True, related_name='+', to='gcyjx.Snjsz'),
        ),
    ]
