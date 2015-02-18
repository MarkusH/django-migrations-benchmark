# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glcmkwkzv', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iwzqe',
            name='lbrkrs',
        ),
        migrations.AddField(
            model_name='iwzqe',
            name='ofhxrdky',
            field=models.IntegerField(default=0),
        ),
    ]
