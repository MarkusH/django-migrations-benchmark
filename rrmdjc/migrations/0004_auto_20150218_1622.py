# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mjdxvqk', '0006_auto_20150218_1622'),
        ('rrmdjc', '0003_ddzxkrvtfd_vlpnxn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gxoqulk',
            name='cimezoiy',
        ),
        migrations.AddField(
            model_name='gxoqulk',
            name='dbvbik',
            field=models.ForeignKey(null=True, related_name='+', to='mjdxvqk.Curcmm'),
        ),
    ]
