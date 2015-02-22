# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ukxhbn', '0005_auto_20150218_1624'),
        ('pnxyvqx', '0008_auto_20150218_1624'),
        ('epbbfwihj', '0011_auto_20150218_1624'),
    ]

    run_before = [
        ('pnxyvqx', '0010_auto_20150218_1627'),
        ('emncdxt', '0007_delete_ktiod'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mmfrlqqf',
        ),
        migrations.RemoveField(
            model_name='zfpgchkbaz',
            name='axmnlbmf',
        ),
        migrations.AddField(
            model_name='apnbivckq',
            name='ghjmssxs',
            field=models.CharField(default='', max_length=58),
        ),
        migrations.AddField(
            model_name='uzdthbetj',
            name='ylfksaoydd',
            field=models.OneToOneField(null=True, related_name='+', to='pnxyvqx.Fmrensoxi'),
        ),
        migrations.AddField(
            model_name='zfpgchkbaz',
            name='ersxh',
            field=models.ForeignKey(null=True, related_name='+', to='ukxhbn.Xqerjvxatp'),
        ),
    ]
