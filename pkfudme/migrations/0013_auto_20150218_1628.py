# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ysgxuyu', '0011_auto_20150218_1628'),
        ('pkfudme', '0012_auto_20150218_1628'),
    ]

    run_before = [
        ('ysgxuyu', '0012_delete_bmovnbnmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jrppdzds',
            name='pwslpi',
        ),
        migrations.AddField(
            model_name='cfjtqbcmjd',
            name='elimafue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='heehdxfqyb',
            name='hbttv',
            field=models.ForeignKey(null=True, related_name='+', to='ysgxuyu.Bmovnbnmed'),
        ),
        migrations.AddField(
            model_name='jrppdzds',
            name='trqdjcjqq',
            field=models.OneToOneField(null=True, related_name='+', to='pkfudme.Ewxxluebq'),
        ),
    ]
