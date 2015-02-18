# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakry', '0012_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flfbdpu',
            name='puzjw',
        ),
        migrations.RemoveField(
            model_name='xgsseizbpr',
            name='fvqktro',
        ),
        migrations.AddField(
            model_name='xgsseizbpr',
            name='kensvdnpij',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Flfbdpu',
        ),
    ]
