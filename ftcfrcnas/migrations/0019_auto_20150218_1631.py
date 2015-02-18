# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emncdxt', '0012_shgjep_qucvdgncbq'),
        ('ftcfrcnas', '0018_auto_20150218_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sukkrqb',
            name='vsgwbct',
        ),
        migrations.AddField(
            model_name='qibygpddzw',
            name='jviyag',
            field=models.CharField(default='', max_length=81),
        ),
        migrations.AddField(
            model_name='sukkrqb',
            name='lbyzkekw',
            field=models.ForeignKey(null=True, related_name='+', to='emncdxt.Ggnqplqy'),
        ),
    ]
