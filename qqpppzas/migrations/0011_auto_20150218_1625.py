# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ysgxuyu', '0007_omtmse_puvofvtb'),
        ('qqpppzas', '0010_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='igtbspg',
            name='fpakgnfxli',
        ),
        migrations.RemoveField(
            model_name='prljmjou',
            name='hiacissed',
        ),
        migrations.AddField(
            model_name='shtlozkm',
            name='wjznogs',
            field=models.OneToOneField(null=True, related_name='+', to='ysgxuyu.Bmovnbnmed'),
        ),
    ]
