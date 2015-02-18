# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuspknbh', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='knkhh',
            name='vubojs',
        ),
        migrations.DeleteModel(
            name='Knkhh',
        ),
    ]
