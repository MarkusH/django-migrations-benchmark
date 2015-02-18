# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digmcd', '0021_lemzs_qaull'),
        ('zhavbmq', '0020_auto_20150218_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='hmaopvcufb',
            name='xssitkonuc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rnddmd',
            name='gdhwm',
            field=models.ForeignKey(null=True, related_name='+', to='digmcd.Rozpduya'),
        ),
    ]
