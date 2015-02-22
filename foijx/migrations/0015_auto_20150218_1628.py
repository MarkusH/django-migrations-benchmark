# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0016_mkihzu'),
        ('foijx', '0014_auto_20150218_1628'),
    ]

    run_before = [
        ('pnxyvqx', '0012_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gsdqrijpp',
            name='akszwqxbr',
        ),
        migrations.RemoveField(
            model_name='qqktwujdfq',
            name='uecimvq',
        ),
        migrations.AddField(
            model_name='abmhnczd',
            name='nflur',
            field=models.ForeignKey(null=True, related_name='+', to='zhavbmq.Rnddmd'),
        ),
        migrations.AddField(
            model_name='cnkdojs',
            name='aezcuq',
            field=models.CharField(default='', max_length=230),
        ),
        migrations.DeleteModel(
            name='Gsdqrijpp',
        ),
    ]
