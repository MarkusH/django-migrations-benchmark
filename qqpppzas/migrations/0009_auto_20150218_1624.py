# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rwlfplwktj', '0006_auto_20150218_1624'),
        ('etnevwmkj', '0007_remove_wpkevitz_eqzsll'),
        ('wulegwfs', '0005_auto_20150218_1623'),
        ('qqpppzas', '0008_auto_20150218_1623'),
    ]

    run_before = [
        ('burhjvc', '0018_auto_20150218_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='igtbspg',
            name='dsqhvnp',
        ),
        migrations.RemoveField(
            model_name='tqlaa',
            name='vcapzn',
        ),
        migrations.RemoveField(
            model_name='xcuutwsyfn',
            name='kykqcsvbz',
        ),
        migrations.AddField(
            model_name='igtbspg',
            name='rhdlydtrdw',
            field=models.ForeignKey(null=True, related_name='+', to='etnevwmkj.Noxqha'),
        ),
        migrations.AddField(
            model_name='tqlaa',
            name='jazakfc',
            field=models.OneToOneField(null=True, related_name='+', to='rwlfplwktj.Thqldbdjm'),
        ),
        migrations.AddField(
            model_name='xcuutwsyfn',
            name='asyjcrv',
            field=models.OneToOneField(null=True, related_name='+', to='wulegwfs.Txgqxz'),
        ),
    ]
