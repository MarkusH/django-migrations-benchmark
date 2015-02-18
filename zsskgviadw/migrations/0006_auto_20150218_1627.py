# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygnakzgjxu', '0008_auto_20150218_1626'),
        ('zsskgviadw', '0005_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ltlsozji',
            name='adcqd',
        ),
        migrations.AddField(
            model_name='cgsmhniqqe',
            name='qshiztddmz',
            field=models.CharField(default='', max_length=76),
        ),
        migrations.AddField(
            model_name='ltlsozji',
            name='djyxf',
            field=models.OneToOneField(null=True, related_name='+', to='ygnakzgjxu.Xdwhlpqgw'),
        ),
    ]
