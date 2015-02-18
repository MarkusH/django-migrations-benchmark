# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtfgy', '0001_initial'),
        ('rrmdjc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bemqls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kiknreazyv', models.ForeignKey(null=True, related_name='+', to='rrmdjc.Gxoqulk')),
            ],
        ),
        migrations.CreateModel(
            name='Rqikftw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sjnjki', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rqzheruyb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xknvpfy', models.ForeignKey(null=True, related_name='+', to='gtfgy.Xqcngusl')),
            ],
        ),
    ]
