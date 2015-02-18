# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burhjvc', '0008_auto_20150218_1622'),
        ('qqpppzas', '0005_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fzhxya',
            name='mvaeauil',
        ),
        migrations.RemoveField(
            model_name='fzhxya',
            name='szryc',
        ),
        migrations.RemoveField(
            model_name='tqlaa',
            name='zezpryllj',
        ),
        migrations.AddField(
            model_name='tqlaa',
            name='vcapzn',
            field=models.ForeignKey(null=True, related_name='+', to='burhjvc.Qbuqivoko'),
        ),
        migrations.DeleteModel(
            name='Fzhxya',
        ),
    ]
