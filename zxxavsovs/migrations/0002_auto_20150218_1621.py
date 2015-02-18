# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zngxahi', '0003_auto_20150218_1621'),
        ('zxxavsovs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kiikphbz',
            name='wtcqvpcl',
        ),
        migrations.AddField(
            model_name='kiikphbz',
            name='hgxjksbg',
            field=models.ForeignKey(null=True, related_name='+', to='zngxahi.Llnksobygh'),
        ),
    ]
