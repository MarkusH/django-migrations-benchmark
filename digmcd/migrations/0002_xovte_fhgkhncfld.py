# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digmcd', '0001_initial'),
        ('tyfslutb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='xovte',
            name='fhgkhncfld',
            field=models.ForeignKey(null=True, related_name='+', to='tyfslutb.Ynbpgqn'),
        ),
    ]
