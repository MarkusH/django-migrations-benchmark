# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zxxavsovs', '0010_auto_20150218_1627'),
    ]

    run_before = [
        ('zngxahi', '0016_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fiellmltob',
            name='cgcyzsjw',
        ),
        migrations.RemoveField(
            model_name='kiikphbz',
            name='hgxjksbg',
        ),
        migrations.AddField(
            model_name='fiellmltob',
            name='gkjqcsmyc',
            field=models.CharField(default='', max_length=22),
        ),
    ]
