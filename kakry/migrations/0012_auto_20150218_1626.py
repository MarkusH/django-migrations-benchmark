# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakry', '0011_lmxjryphro_opnuy'),
    ]

    run_before = [
        ('adlorvp', '0017_auto_20150218_1630'),
        ('gcyjx', '0010_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aefqhqkmm',
            name='yupnznks',
        ),
        migrations.RemoveField(
            model_name='lmxjryphro',
            name='nlxhwbmf',
        ),
        migrations.RemoveField(
            model_name='xgsseizbpr',
            name='ylttnfe',
        ),
        migrations.DeleteModel(
            name='Aefqhqkmm',
        ),
    ]
