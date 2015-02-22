# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glcmkwkzv', '0010_auto_20150218_1626'),
        ('wyxbcga', '0010_auto_20150218_1625'),
    ]

    run_before = [
        ('kakry', '0012_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gmclwtufhi',
            name='qjfhzntzm',
        ),
        migrations.RemoveField(
            model_name='oblwdacdf',
            name='snjlwam',
        ),
        migrations.AddField(
            model_name='gmclwtufhi',
            name='agejdpoju',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jkjvvohe',
            name='hszww',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='oblwdacdf',
            name='ohjnftmzh',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rsaiyadejv',
            name='aabsvd',
            field=models.OneToOneField(null=True, related_name='+', to='glcmkwkzv.Idmamodyjp'),
        ),
    ]
