# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rwlfplwktj', '0001_initial'),
        ('ruvaymw', '0001_initial'),
        ('digmcd', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='gxovs',
            name='ovvkibpppv',
            field=models.ForeignKey(null=True, related_name='+', to='ruvaymw.Ndhcup'),
        ),
        migrations.AddField(
            model_name='rdfrrg',
            name='jytqslm',
            field=models.CharField(default='', max_length=55),
        ),
        migrations.AddField(
            model_name='untgafvod',
            name='upmuq',
            field=models.OneToOneField(null=True, related_name='+', to='rwlfplwktj.Knoeepjnhs'),
        ),
    ]
