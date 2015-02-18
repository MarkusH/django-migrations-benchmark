# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakry', '0010_auto_20150218_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='lmxjryphro',
            name='opnuy',
            field=models.CharField(default='', max_length=76),
        ),
    ]
