# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epbbfwihj', '0010_auto_20150218_1623'),
        ('burhjvc', '0010_aziftfctf_splbqgxm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qbuqivoko',
            name='xfdapna',
        ),
        migrations.AddField(
            model_name='qbuqivoko',
            name='orrjz',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qwtnucajp',
            name='efhmvghs',
            field=models.OneToOneField(null=True, related_name='+', to='epbbfwihj.Wcklq'),
        ),
        migrations.AddField(
            model_name='ydprem',
            name='gjmyvkze',
            field=models.IntegerField(default=0),
        ),
    ]
