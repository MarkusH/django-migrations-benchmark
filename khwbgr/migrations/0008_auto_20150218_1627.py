# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burhjvc', '0015_auto_20150218_1627'),
        ('khwbgr', '0007_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ibuazau',
            name='uutjmgjxmy',
        ),
        migrations.AddField(
            model_name='ibuazau',
            name='qygkfxppc',
            field=models.OneToOneField(null=True, related_name='+', to='burhjvc.Oilvk'),
        ),
    ]
