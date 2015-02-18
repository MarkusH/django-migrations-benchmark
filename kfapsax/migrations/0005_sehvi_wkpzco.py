# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuspknbh', '0011_auto_20150218_1625'),
        ('kfapsax', '0004_remove_sehvi_wspsk'),
    ]

    operations = [
        migrations.AddField(
            model_name='sehvi',
            name='wkpzco',
            field=models.ForeignKey(null=True, related_name='+', to='cuspknbh.Yicalotegs'),
        ),
    ]
