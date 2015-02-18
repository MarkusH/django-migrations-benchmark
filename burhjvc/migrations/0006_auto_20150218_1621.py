# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yiupu', '0003_auto_20150218_1621'),
        ('burhjvc', '0005_remove_ydprem_npbbb'),
    ]

    operations = [
        migrations.AddField(
            model_name='qbuqivoko',
            name='xfdapna',
            field=models.OneToOneField(null=True, related_name='+', to='yiupu.Zzsheqzf'),
        ),
        migrations.AddField(
            model_name='ydprem',
            name='wuxfyceg',
            field=models.IntegerField(default=0),
        ),
    ]
