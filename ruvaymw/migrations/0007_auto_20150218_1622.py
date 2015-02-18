# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etnevwmkj', '0004_auto_20150218_1622'),
        ('emncdxt', '0005_mioxdvg_rzvpibb'),
        ('ruvaymw', '0006_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqagt',
            name='vtnbt',
        ),
        migrations.RemoveField(
            model_name='hhnwphllci',
            name='akuhjv',
        ),
        migrations.AddField(
            model_name='faqagt',
            name='kasjcjsp',
            field=models.ForeignKey(null=True, related_name='+', to='emncdxt.Yvgnpangr'),
        ),
        migrations.AddField(
            model_name='hhnwphllci',
            name='lgfcdtfmmh',
            field=models.ForeignKey(null=True, related_name='+', to='etnevwmkj.Noxqha'),
        ),
    ]
