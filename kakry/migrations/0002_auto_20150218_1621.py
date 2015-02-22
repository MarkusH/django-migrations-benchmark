# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emncdxt', '0003_mioxdvg_uobgln'),
        ('irmtbds', '0001_initial'),
        ('cuspknbh', '0002_auto_20150218_1621'),
        ('kakry', '0001_initial'),
        ('ftcfrcnas', '0002_lqfdippdc_cjqbkmmoe'),
        ('qclaxc', '0001_initial'),
    ]

    run_before = [
        ('qclaxc', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='mfivvxhds',
            name='dlcolp',
            field=models.ForeignKey(null=True, related_name='+', to='qclaxc.Rmtucrztaq'),
        ),
        migrations.AddField(
            model_name='lmxjryphro',
            name='kkqmbqbmvt',
            field=models.OneToOneField(null=True, related_name='+', to='emncdxt.Yvgnpangr'),
        ),
        migrations.AddField(
            model_name='kiurw',
            name='fjzlxklz',
            field=models.ForeignKey(null=True, related_name='+', to='irmtbds.Rqikftw'),
        ),
        migrations.AddField(
            model_name='flfbdpu',
            name='puzjw',
            field=models.OneToOneField(null=True, related_name='+', to='ftcfrcnas.Iwhkq'),
        ),
        migrations.AddField(
            model_name='ajbkovws',
            name='rlsejr',
            field=models.ForeignKey(null=True, related_name='+', to='cuspknbh.Djbbtxk'),
        ),
    ]
