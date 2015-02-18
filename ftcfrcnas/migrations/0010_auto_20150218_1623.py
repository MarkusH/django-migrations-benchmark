# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emncdxt', '0005_mioxdvg_rzvpibb'),
        ('ftcfrcnas', '0009_auto_20150218_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kkkuodosbi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guvfa', models.CharField(default='', max_length=203)),
            ],
        ),
        migrations.RemoveField(
            model_name='iwhkq',
            name='bqlssqo',
        ),
        migrations.AddField(
            model_name='cdardz',
            name='bfoseuwjhw',
            field=models.OneToOneField(null=True, related_name='+', to='emncdxt.Ktiod'),
        ),
    ]
