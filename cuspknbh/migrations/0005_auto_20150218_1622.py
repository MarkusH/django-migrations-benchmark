# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuspknbh', '0004_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='djbbtxk',
            name='soayvwcin',
        ),
        migrations.AddField(
            model_name='djbbtxk',
            name='szwaxyb',
            field=models.CharField(default='', max_length=178),
        ),
    ]
