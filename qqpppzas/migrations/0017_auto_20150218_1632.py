# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qqpppzas', '0016_auto_20150218_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tqlaa',
            name='jazakfc',
        ),
        migrations.AddField(
            model_name='ybcxw',
            name='yxgvh',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Tqlaa',
        ),
    ]
