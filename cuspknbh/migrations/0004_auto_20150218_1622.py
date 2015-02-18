# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuspknbh', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glbtwo',
            name='hdlrbpj',
        ),
        migrations.DeleteModel(
            name='Glbtwo',
        ),
    ]
