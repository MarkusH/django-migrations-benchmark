# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcfrcnas', '0010_auto_20150218_1623'),
        ('wawqcpvrz', '0005_xivomw_lramz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nrmckl',
            name='esgced',
        ),
        migrations.AddField(
            model_name='nrmckl',
            name='ktoflmfxp',
            field=models.OneToOneField(null=True, related_name='+', to='ftcfrcnas.Qrwqtj'),
        ),
    ]
