# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burhjvc', '0017_auto_20150218_1628'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Qbuqivoko',
        ),
        migrations.RemoveField(
            model_name='bewsptdyqv',
            name='xeqlaepw',
        ),
        migrations.AddField(
            model_name='bewsptdyqv',
            name='qwvtzko',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ubeubsuez',
            name='jowmt',
            field=models.CharField(default='', max_length=9),
        ),
    ]
