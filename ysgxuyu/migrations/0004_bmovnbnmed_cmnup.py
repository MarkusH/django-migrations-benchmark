# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ysgxuyu', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmovnbnmed',
            name='cmnup',
            field=models.CharField(default='', max_length=30),
        ),
    ]
