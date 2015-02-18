# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digmcd', '0010_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arqcdv',
            name='cffdghbzam',
        ),
        migrations.AddField(
            model_name='zyjgcrtsvt',
            name='pwgdlxtg',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Arqcdv',
        ),
    ]
