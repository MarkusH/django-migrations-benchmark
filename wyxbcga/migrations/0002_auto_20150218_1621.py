# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyxbcga', '0001_initial'),
    ]

    run_before = [
        ('yiupu', '0002_delete_jpmwh'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eezxvbbvmn',
            name='redlewthb',
        ),
        migrations.RemoveField(
            model_name='ojshxdt',
            name='fakazhjh',
        ),
    ]
