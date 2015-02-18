# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0006_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bdniaupe',
            name='plgvgy',
        ),
        migrations.RemoveField(
            model_name='hmaopvcufb',
            name='xciop',
        ),
        migrations.AddField(
            model_name='bdniaupe',
            name='nftecr',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hmaopvcufb',
            name='bjmgm',
            field=models.CharField(default='', max_length=187),
        ),
    ]
