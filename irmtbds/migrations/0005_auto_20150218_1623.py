# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irmtbds', '0004_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bemqls',
            name='aedocfocsn',
        ),
        migrations.AddField(
            model_name='bemqls',
            name='bjknddubg',
            field=models.IntegerField(default=0),
        ),
    ]
