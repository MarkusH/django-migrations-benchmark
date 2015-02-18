# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burhjvc', '0006_auto_20150218_1621'),
        ('cuspknbh', '0003_auto_20150218_1621'),
        ('qqpppzas', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='fzhxya',
            name='szryc',
            field=models.OneToOneField(null=True, related_name='+', to='burhjvc.Pdzdhpq'),
        ),
        migrations.AddField(
            model_name='mukbde',
            name='rmdjmdwewd',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vdscpy',
            name='mxjhvnbbqm',
            field=models.OneToOneField(null=True, related_name='+', to='cuspknbh.Glbtwo'),
        ),
    ]
