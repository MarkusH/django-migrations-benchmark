# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burhjvc', '0008_auto_20150218_1622'),
        ('mjdxvqk', '0005_vmnilim_rvflb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waktrjgi',
            name='tssfc',
        ),
        migrations.AddField(
            model_name='waktrjgi',
            name='qrwndvxmf',
            field=models.OneToOneField(null=True, related_name='+', to='burhjvc.Pdzdhpq'),
        ),
    ]
