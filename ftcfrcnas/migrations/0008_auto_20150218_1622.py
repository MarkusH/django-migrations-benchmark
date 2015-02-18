# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygnakzgjxu', '0004_xdwhlpqgw'),
        ('ftcfrcnas', '0007_auto_20150218_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='iwhkq',
            name='xtdreu',
            field=models.CharField(default='', max_length=87),
        ),
        migrations.AddField(
            model_name='wjxepwd',
            name='jxowe',
            field=models.ForeignKey(null=True, related_name='+', to='ygnakzgjxu.Xpmnn'),
        ),
    ]
