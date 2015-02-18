# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcyjx', '0001_initial'),
        ('qqpppzas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ybcxw',
            name='mwpkhqrbva',
        ),
        migrations.AddField(
            model_name='ybcxw',
            name='vkqhycup',
            field=models.ForeignKey(null=True, related_name='+', to='gcyjx.Snjsz'),
        ),
    ]
