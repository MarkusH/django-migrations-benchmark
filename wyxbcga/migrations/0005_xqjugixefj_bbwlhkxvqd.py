# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ysgxuyu', '0005_auto_20150218_1622'),
        ('wyxbcga', '0004_remove_xqjugixefj_xvbpvsvwrw'),
    ]

    operations = [
        migrations.AddField(
            model_name='xqjugixefj',
            name='bbwlhkxvqd',
            field=models.OneToOneField(null=True, related_name='+', to='ysgxuyu.Bmovnbnmed'),
        ),
    ]
