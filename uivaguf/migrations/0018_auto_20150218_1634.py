# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uivaguf', '0017_auto_20150218_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zwjgfcdi',
            name='crkhxew',
        ),
        migrations.AddField(
            model_name='zwjgfcdi',
            name='kxhlvqrh',
            field=models.CharField(default='', max_length=127),
        ),
    ]
