# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyxbcga', '0001_initial'),
        ('yiupu', '0001_initial'),
        ('gcyjx', '0001_initial'),
        ('ruvaymw', '0001_initial'),
        ('qclaxc', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dipxet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nwammqlaq', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Edynlg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vitmzurb', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Jydvnf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xwilqwztoj', models.ForeignKey(null=True, related_name='+', to='qclaxc.Pmcbxoetr')),
            ],
        ),
        migrations.CreateModel(
            name='Kihvqrmtr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llmloxxmss', models.ForeignKey(null=True, related_name='+', to='gcyjx.Ivcsuscyb')),
            ],
        ),
        migrations.CreateModel(
            name='Ligxr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rgamodph', models.OneToOneField(null=True, related_name='+', to='ruvaymw.Owamswc')),
            ],
        ),
        migrations.CreateModel(
            name='Nzfoyhj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hwflnm', models.ForeignKey(null=True, related_name='+', to='yiupu.Fzmiecxuo')),
            ],
        ),
        migrations.CreateModel(
            name='Oqyncxevyj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lykvcrgp', models.CharField(default='', max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Ssalb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eelqndo', models.ForeignKey(null=True, related_name='+', to='wyxbcga.Ojshxdt')),
            ],
        ),
    ]
