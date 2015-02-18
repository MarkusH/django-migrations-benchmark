# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ysgxuyu', '0013_auto_20150218_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eppkc',
            name='fdjqgbumm',
        ),
        migrations.AddField(
            model_name='njigbqwuqa',
            name='xorsf',
            field=models.CharField(default='', max_length=184),
        ),
        migrations.DeleteModel(
            name='Eppkc',
        ),
    ]
