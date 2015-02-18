# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ysgxuyu', '0009_remove_bmovnbnmed_cmnup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bmovnbnmed',
            name='zczgojzvsb',
        ),
        migrations.AddField(
            model_name='bmovnbnmed',
            name='dstfkls',
            field=models.CharField(default='', max_length=77),
        ),
    ]
