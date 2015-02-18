# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uivaguf', '0002_auto_20150218_1621'),
        ('bniworfy', '0004_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dkvkm',
            name='nteqflev',
        ),
        migrations.AddField(
            model_name='dkvkm',
            name='gbgkdcxxve',
            field=models.ForeignKey(null=True, related_name='+', to='uivaguf.Bqjxljlwq'),
        ),
    ]
