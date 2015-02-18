# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apbqku', '0004_ffussl_rgwaklwvyx'),
        ('epbbfwihj', '0004_auto_20150218_1621'),
        ('joavhqi', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lfssmpr',
            name='ulnuig',
        ),
        migrations.RemoveField(
            model_name='rdhhdq',
            name='ztnjkzyby',
        ),
        migrations.AddField(
            model_name='lfssmpr',
            name='qweppfqt',
            field=models.ForeignKey(null=True, related_name='+', to='apbqku.Ffussl'),
        ),
        migrations.AddField(
            model_name='rdhhdq',
            name='yhhsrszrp',
            field=models.OneToOneField(null=True, related_name='+', to='epbbfwihj.Apnbivckq'),
        ),
    ]
