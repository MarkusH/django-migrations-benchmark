# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emncdxt', '0008_auto_20150218_1626'),
        ('yiupu', '0004_auto_20150218_1623'),
        ('ruvaymw', '0013_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yckccoccsv',
            name='jmdxrunl',
        ),
        migrations.AddField(
            model_name='faqagt',
            name='whygf',
            field=models.OneToOneField(null=True, related_name='+', to='yiupu.Zzsheqzf'),
        ),
        migrations.AddField(
            model_name='yckccoccsv',
            name='bhxiqpohj',
            field=models.OneToOneField(null=True, related_name='+', to='emncdxt.Yvgnpangr'),
        ),
    ]
