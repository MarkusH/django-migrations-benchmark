# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavygg', '0012_remove_ligxr_kfznkinf'),
    ]

    run_before = [
        ('uivaguf', '0013_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kihvqrmtr',
            name='lxnjosrj',
        ),
        migrations.AddField(
            model_name='hitvmegxki',
            name='moyjguzq',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Kihvqrmtr',
        ),
    ]
