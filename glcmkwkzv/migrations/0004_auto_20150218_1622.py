# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glcmkwkzv', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iwzqe',
            name='ofhxrdky',
        ),
        migrations.AddField(
            model_name='iwzqe',
            name='smyorbp',
            field=models.IntegerField(default=0),
        ),
    ]
