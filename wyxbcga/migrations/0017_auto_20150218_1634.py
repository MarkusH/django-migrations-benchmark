# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyxbcga', '0016_remove_qqpfvbjbpk_ebcai'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='begquxerkm',
            name='uxdnq',
        ),
        migrations.RemoveField(
            model_name='ojshxdt',
            name='xnslxqkne',
        ),
        migrations.AddField(
            model_name='begquxerkm',
            name='sgwqndjc',
            field=models.OneToOneField(null=True, related_name='+', to='wyxbcga.Rsaiyadejv'),
        ),
        migrations.AddField(
            model_name='ojshxdt',
            name='rrwiqo',
            field=models.IntegerField(default=0),
        ),
    ]
