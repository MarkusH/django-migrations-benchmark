# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geemkrwi', '0014_auto_20150218_1628'),
        ('cuspknbh', '0014_estwpd'),
    ]

    operations = [
        migrations.AddField(
            model_name='estwpd',
            name='abdlqrp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ufrkff',
            name='wxfwt',
            field=models.ForeignKey(null=True, related_name='+', to='geemkrwi.Mxvmqmhku'),
        ),
    ]
