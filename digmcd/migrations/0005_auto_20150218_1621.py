# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epbbfwihj', '0003_auto_20150218_1621'),
        ('apbqku', '0004_ffussl_rgwaklwvyx'),
        ('digmcd', '0004_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rdfrrg',
            name='jytqslm',
        ),
        migrations.RemoveField(
            model_name='zaganduq',
            name='qwnmi',
        ),
        migrations.AddField(
            model_name='rdfrrg',
            name='lihyfbg',
            field=models.ForeignKey(null=True, related_name='+', to='apbqku.Ssgsglh'),
        ),
        migrations.AddField(
            model_name='zaganduq',
            name='kmmmtnspx',
            field=models.OneToOneField(null=True, related_name='+', to='epbbfwihj.Uzdthbetj'),
        ),
    ]
