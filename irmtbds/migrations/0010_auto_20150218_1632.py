# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irmtbds', '0009_delete_bemqls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='islmbaqxc',
            name='yqxhdtazhk',
        ),
        migrations.DeleteModel(
            name='Islmbaqxc',
        ),
    ]
