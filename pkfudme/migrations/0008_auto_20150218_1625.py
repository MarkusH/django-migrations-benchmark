# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkfudme', '0007_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbpile',
            name='yamkggnk',
        ),
        migrations.RemoveField(
            model_name='mnvmeraq',
            name='gutje',
        ),
        migrations.AddField(
            model_name='cfjtqbcmjd',
            name='smrdaj',
            field=models.CharField(default='', max_length=187),
        ),
        migrations.AddField(
            model_name='dbpile',
            name='ynyiuist',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mnvmeraq',
            name='qmpes',
            field=models.IntegerField(default=0),
        ),
    ]
