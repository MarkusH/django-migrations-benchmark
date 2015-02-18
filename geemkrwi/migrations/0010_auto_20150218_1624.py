# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcfrcnas', '0011_auto_20150218_1624'),
        ('geemkrwi', '0009_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='egvtran',
            name='iaywdnrfj',
        ),
        migrations.RemoveField(
            model_name='hxkigetost',
            name='vixlvfvme',
        ),
        migrations.RemoveField(
            model_name='uqqgcprwn',
            name='mciutq',
        ),
        migrations.AddField(
            model_name='hxkigetost',
            name='wnrwf',
            field=models.ForeignKey(null=True, related_name='+', to='ftcfrcnas.Wjxepwd'),
        ),
        migrations.AddField(
            model_name='uqqgcprwn',
            name='cordori',
            field=models.CharField(default='', max_length=51),
        ),
        migrations.AddField(
            model_name='wilsmoea',
            name='ssyao',
            field=models.CharField(default='', max_length=223),
        ),
    ]
