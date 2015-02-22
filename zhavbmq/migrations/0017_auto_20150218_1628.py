# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsrp', '0008_auto_20150218_1628'),
        ('ysgxuyu', '0011_auto_20150218_1628'),
        ('zhavbmq', '0016_mkihzu'),
    ]

    run_before = [
        ('cmsrp', '0009_auto_20150218_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hmaopvcufb',
            name='bjmgm',
        ),
        migrations.RemoveField(
            model_name='rnddmd',
            name='ofhma',
        ),
        migrations.RemoveField(
            model_name='ybkewg',
            name='fuiqe',
        ),
        migrations.AddField(
            model_name='hmaopvcufb',
            name='wnxwji',
            field=models.OneToOneField(null=True, related_name='+', to='cmsrp.Vlmfay'),
        ),
        migrations.AddField(
            model_name='rnddmd',
            name='utxzk',
            field=models.ForeignKey(null=True, related_name='+', to='ysgxuyu.Omtmse'),
        ),
        migrations.AddField(
            model_name='ybkewg',
            name='ufxsdkepdu',
            field=models.CharField(default='', max_length=78),
        ),
    ]
