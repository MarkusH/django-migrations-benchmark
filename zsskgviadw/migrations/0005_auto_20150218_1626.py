# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkfudme', '0010_auto_20150218_1626'),
        ('gbsaqmaxu', '0013_auto_20150218_1626'),
        ('zsskgviadw', '0004_auto_20150218_1622'),
    ]

    run_before = [
        ('gbsaqmaxu', '0014_auto_20150218_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cgsmhniqqe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rqkbhz', models.OneToOneField(null=True, related_name='+', to='pkfudme.Cfjtqbcmjd')),
            ],
        ),
        migrations.RemoveField(
            model_name='ltlsozji',
            name='nhiafkfonb',
        ),
        migrations.AddField(
            model_name='ltlsozji',
            name='adcqd',
            field=models.ForeignKey(null=True, related_name='+', to='gbsaqmaxu.Lshmrghvzw'),
        ),
    ]
