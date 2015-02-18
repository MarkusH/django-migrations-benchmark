# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avwpufexob', '0005_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ubpmj',
            name='itflucbh',
        ),
        migrations.RemoveField(
            model_name='ubpmj',
            name='ktwasnimoe',
        ),
        migrations.DeleteModel(
            name='Ubpmj',
        ),
    ]
