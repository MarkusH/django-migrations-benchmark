# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gbsaqmaxu', '0004_utfwgx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zdahw',
            name='binimm',
        ),
        migrations.RemoveField(
            model_name='knqau',
            name='lctemiulg',
        ),
        migrations.AddField(
            model_name='knqau',
            name='tmrsfefj',
            field=models.CharField(default='', max_length=159),
        ),
        migrations.DeleteModel(
            name='Zdahw',
        ),
    ]
