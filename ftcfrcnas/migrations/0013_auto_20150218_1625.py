# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnxyvqx', '0008_auto_20150218_1624'),
        ('ftcfrcnas', '0012_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cdardz',
            name='emduh',
        ),
        migrations.AddField(
            model_name='cdardz',
            name='hmjcjayr',
            field=models.ForeignKey(null=True, related_name='+', to='pnxyvqx.Aehywz'),
        ),
        migrations.AddField(
            model_name='qibygpddzw',
            name='smhmvshun',
            field=models.IntegerField(default=0),
        ),
    ]
