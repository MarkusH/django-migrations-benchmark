# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ukxhbn', '0003_delete_xtmekz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dcphul',
            name='aschcos',
        ),
        migrations.DeleteModel(
            name='Dcphul',
        ),
    ]
