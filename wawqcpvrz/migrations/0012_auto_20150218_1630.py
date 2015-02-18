# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digmcd', '0018_auto_20150218_1630'),
        ('wawqcpvrz', '0011_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nqohhreonm',
            name='rwniop',
        ),
        migrations.RemoveField(
            model_name='scfuekgkl',
            name='rhgqd',
        ),
        migrations.AddField(
            model_name='nqohhreonm',
            name='lojmqltr',
            field=models.ForeignKey(null=True, related_name='+', to='digmcd.Yymzlvsz'),
        ),
        migrations.AddField(
            model_name='scfuekgkl',
            name='bgucm',
            field=models.CharField(default='', max_length=175),
        ),
    ]
