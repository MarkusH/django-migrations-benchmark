# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mntrwrm', '0009_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eaeehqi',
            name='stfgtnuej',
        ),
        migrations.DeleteModel(
            name='Eaeehqi',
        ),
    ]
