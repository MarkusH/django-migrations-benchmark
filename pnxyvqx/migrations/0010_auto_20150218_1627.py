# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uivaguf', '0014_auto_20150218_1627'),
        ('pnxyvqx', '0009_fmrensoxi_gserouu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fmrensoxi',
            name='kdnkbk',
        ),
        migrations.RemoveField(
            model_name='aehywz',
            name='hqjnudya',
        ),
        migrations.AddField(
            model_name='nenfvguk',
            name='yglmn',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rwrraj',
            name='qbdud',
            field=models.OneToOneField(null=True, related_name='+', to='uivaguf.Zwjgfcdi'),
        ),
        migrations.DeleteModel(
            name='Fmrensoxi',
        ),
    ]
