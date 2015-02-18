# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkfudme', '0006_auto_20150218_1622'),
        ('ysgxuyu', '0005_auto_20150218_1622'),
        ('adlorvp', '0008_delete_tpxhcuni'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kmygwyorsi',
            name='zvqajqzsmi',
        ),
        migrations.RemoveField(
            model_name='kzrfnfxko',
            name='fmvbwiqgc',
        ),
        migrations.AddField(
            model_name='kmygwyorsi',
            name='albva',
            field=models.ForeignKey(null=True, related_name='+', to='ysgxuyu.Bmovnbnmed'),
        ),
        migrations.AddField(
            model_name='kzrfnfxko',
            name='conaco',
            field=models.OneToOneField(null=True, related_name='+', to='pkfudme.Ewxxluebq'),
        ),
    ]
