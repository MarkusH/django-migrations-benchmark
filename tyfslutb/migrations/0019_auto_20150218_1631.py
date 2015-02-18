# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyfslutb', '0018_remove_juemb_nwqygyqwxc'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Djnppzsr',
        ),
        migrations.RemoveField(
            model_name='ixmfsgch',
            name='lwczoav',
        ),
        migrations.AddField(
            model_name='ixmfsgch',
            name='wwkkhdlw',
            field=models.CharField(default='', max_length=201),
        ),
        migrations.AddField(
            model_name='juemb',
            name='lextgfnkk',
            field=models.IntegerField(default=0),
        ),
    ]
