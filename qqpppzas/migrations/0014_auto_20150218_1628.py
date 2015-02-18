# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qclaxc', '0015_auto_20150218_1628'),
        ('qqpppzas', '0013_auto_20150218_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fngqkhhe',
            name='bsvigtdmwm',
        ),
        migrations.AddField(
            model_name='fngqkhhe',
            name='cgmxqscs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mukbde',
            name='lzkmi',
            field=models.ForeignKey(null=True, related_name='+', to='qclaxc.Jvoopceqsv'),
        ),
        migrations.AddField(
            model_name='ybcxw',
            name='vstfeyikg',
            field=models.CharField(default='', max_length=174),
        ),
    ]
