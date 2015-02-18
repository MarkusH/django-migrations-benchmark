# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epbbfwihj', '0014_auto_20150218_1627'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Uzdthbetj',
        ),
        migrations.RemoveField(
            model_name='uwaayy',
            name='jtpsyn',
        ),
        migrations.AddField(
            model_name='uwaayy',
            name='wojspu',
            field=models.IntegerField(default=0),
        ),
    ]
