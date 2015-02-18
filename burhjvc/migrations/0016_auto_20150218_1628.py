# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burhjvc', '0015_auto_20150218_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qbuqivoko',
            name='vupdohnyr',
        ),
        migrations.AddField(
            model_name='qbuqivoko',
            name='kddwhakvpm',
            field=models.CharField(default='', max_length=231),
        ),
    ]
