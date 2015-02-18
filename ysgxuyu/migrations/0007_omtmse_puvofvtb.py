# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ysgxuyu', '0006_auto_20150218_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='omtmse',
            name='puvofvtb',
            field=models.IntegerField(default=0),
        ),
    ]
