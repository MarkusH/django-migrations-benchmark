# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burhjvc', '0014_remove_qwtnucajp_efhmvghs'),
        ('tyfslutb', '0013_remove_ynbpgqn_ninzjz'),
    ]

    run_before = [
        ('kakry', '0012_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juemb',
            name='behscfzjv',
        ),
        migrations.RemoveField(
            model_name='qcwbo',
            name='nevqtm',
        ),
        migrations.RemoveField(
            model_name='ynbpgqn',
            name='rtmpcyteit',
        ),
        migrations.AddField(
            model_name='juemb',
            name='nwqygyqwxc',
            field=models.OneToOneField(null=True, related_name='+', to='burhjvc.Qbuqivoko'),
        ),
    ]
