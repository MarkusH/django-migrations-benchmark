# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kfapsax', '0005_sehvi_wkpzco'),
        ('uivaguf', '0010_auto_20150218_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blekqwd',
            name='jvdlv',
        ),
        migrations.AddField(
            model_name='blekqwd',
            name='kcyvgyu',
            field=models.ForeignKey(null=True, related_name='+', to='kfapsax.Kmwzcb'),
        ),
    ]
