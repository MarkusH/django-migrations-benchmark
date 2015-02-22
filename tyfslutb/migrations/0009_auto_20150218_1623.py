# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnxyvqx', '0006_aehywz_yehjk'),
        ('gtfgy', '0010_auto_20150218_1623'),
        ('qqpppzas', '0008_auto_20150218_1623'),
        ('emncdxt', '0005_mioxdvg_rzvpibb'),
        ('tyfslutb', '0008_qcwbo_rbasnbzoz'),
    ]

    run_before = [
        ('digmcd', '0011_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ckvpx',
            name='jjgracphi',
        ),
        migrations.RemoveField(
            model_name='juemb',
            name='ldineuo',
        ),
        migrations.RemoveField(
            model_name='qcwbo',
            name='dokqdbprt',
        ),
        migrations.RemoveField(
            model_name='qcwbo',
            name='rbasnbzoz',
        ),
        migrations.AddField(
            model_name='ckvpx',
            name='necukbga',
            field=models.OneToOneField(null=True, related_name='+', to='pnxyvqx.Nenfvguk'),
        ),
        migrations.AddField(
            model_name='cvzmphnk',
            name='bcxikdtwa',
            field=models.OneToOneField(null=True, related_name='+', to='gtfgy.Niwaoqfft'),
        ),
        migrations.AddField(
            model_name='juemb',
            name='behscfzjv',
            field=models.ForeignKey(null=True, related_name='+', to='emncdxt.Yvgnpangr'),
        ),
        migrations.AddField(
            model_name='ynbpgqn',
            name='ninzjz',
            field=models.ForeignKey(null=True, related_name='+', to='qqpppzas.Fngqkhhe'),
        ),
    ]
