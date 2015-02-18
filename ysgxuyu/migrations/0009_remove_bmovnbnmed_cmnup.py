# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ysgxuyu', '0008_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bmovnbnmed',
            name='cmnup',
        ),
    ]
