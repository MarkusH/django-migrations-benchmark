# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esznwrr', '0005_auto_20150218_1625'),
        ('bniworfy', '0015_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gsmbfohda',
            name='gxvwzvtps',
        ),
        migrations.AddField(
            model_name='gsmbfohda',
            name='bholxclp',
            field=models.ForeignKey(null=True, related_name='+', to='esznwrr.Kgrzxxm'),
        ),
    ]
