# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0001_initial'),
        ('emncdxt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shgjep',
            name='hlamaptyhd',
            field=models.OneToOneField(null=True, related_name='+', to='foijx.Wrafoshzom'),
        ),
    ]
