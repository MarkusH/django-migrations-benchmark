# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0018_auto_20150218_1630'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bdniaupe',
        ),
        migrations.RemoveField(
            model_name='rywmfrbmil',
            name='qnkkkea',
        ),
        migrations.AddField(
            model_name='rywmfrbmil',
            name='ikcfhtdxbs',
            field=models.CharField(default='', max_length=9),
        ),
    ]
