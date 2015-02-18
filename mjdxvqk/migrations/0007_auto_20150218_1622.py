# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyxbcga', '0004_remove_xqjugixefj_xvbpvsvwrw'),
        ('mjdxvqk', '0006_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waktrjgi',
            name='qrwndvxmf',
        ),
        migrations.AddField(
            model_name='edugsywcj',
            name='nvhgs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ovbcnxcwyr',
            name='usxwgvyiz',
            field=models.ForeignKey(null=True, related_name='+', to='wyxbcga.Rsaiyadejv'),
        ),
        migrations.DeleteModel(
            name='Waktrjgi',
        ),
    ]
