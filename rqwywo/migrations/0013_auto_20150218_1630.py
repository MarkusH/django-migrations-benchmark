# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zngxahi', '0016_auto_20150218_1628'),
        ('rqwywo', '0012_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mahcgzunnb',
            name='jytvvd',
        ),
        migrations.RemoveField(
            model_name='wmvmz',
            name='lincd',
        ),
        migrations.AddField(
            model_name='mahcgzunnb',
            name='poqdtc',
            field=models.CharField(default='', max_length=194),
        ),
        migrations.AddField(
            model_name='trhinrdlr',
            name='mcuktvuoy',
            field=models.ForeignKey(null=True, related_name='+', to='zngxahi.Hiqedajgiu'),
        ),
        migrations.AddField(
            model_name='wmvmz',
            name='xpvpigphfl',
            field=models.CharField(default='', max_length=67),
        ),
    ]
