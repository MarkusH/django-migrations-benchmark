# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esznwrr', '0005_auto_20150218_1625'),
        ('uivaguf', '0015_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bqjxljlwq',
            name='veqvxofwt',
        ),
        migrations.AddField(
            model_name='bqjxljlwq',
            name='grfqexqela',
            field=models.OneToOneField(null=True, related_name='+', to='esznwrr.Kgrzxxm'),
        ),
    ]
