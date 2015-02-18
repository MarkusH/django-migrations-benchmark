# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohutfvb', '0011_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livljpedso',
            name='ceudc',
        ),
        migrations.AddField(
            model_name='livljpedso',
            name='dbrjj',
            field=models.CharField(default='', max_length=89),
        ),
    ]
