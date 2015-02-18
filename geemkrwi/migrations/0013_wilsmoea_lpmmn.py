# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geemkrwi', '0012_auto_20150218_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='wilsmoea',
            name='lpmmn',
            field=models.CharField(default='', max_length=240),
        ),
    ]
