# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnxyvqx', '0014_auto_20150218_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecatm',
            name='qqhiw',
        ),
        migrations.AddField(
            model_name='ecatm',
            name='mzbldbvpkf',
            field=models.IntegerField(default=0),
        ),
    ]
