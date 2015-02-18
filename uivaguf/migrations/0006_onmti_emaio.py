# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uivaguf', '0005_zwjgfcdi_jprqprkcn'),
    ]

    operations = [
        migrations.AddField(
            model_name='onmti',
            name='emaio',
            field=models.CharField(default='', max_length=172),
        ),
    ]
