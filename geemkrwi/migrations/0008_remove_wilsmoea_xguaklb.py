# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geemkrwi', '0007_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wilsmoea',
            name='xguaklb',
        ),
    ]
