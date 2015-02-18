# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuspknbh', '0015_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='djbbtxk',
            name='nafoj',
        ),
        migrations.RemoveField(
            model_name='mbcah',
            name='auvyvqhx',
        ),
        migrations.AddField(
            model_name='djbbtxk',
            name='zuxnuezt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mbcah',
            name='iibcl',
            field=models.CharField(default='', max_length=1),
        ),
    ]
