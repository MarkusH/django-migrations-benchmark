# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yiupu', '0003_auto_20150218_1621'),
        ('mntrwrm', '0003_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rbhubw',
            name='wcetzzr',
        ),
        migrations.AddField(
            model_name='xevahddk',
            name='aheutab',
            field=models.ForeignKey(null=True, related_name='+', to='yiupu.Zzsheqzf'),
        ),
    ]
