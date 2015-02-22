# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0019_auto_20150218_1631'),
    ]

    run_before = [
        ('cmsrp', '0009_auto_20150218_1632'),
        ('ysgxuyu', '0013_auto_20150218_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hmaopvcufb',
            name='wnxwji',
        ),
        migrations.RemoveField(
            model_name='rnddmd',
            name='utxzk',
        ),
    ]
