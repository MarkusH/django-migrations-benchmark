# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wawqcpvrz', '0001_initial'),
        ('rrmdjc', '0001_initial'),
        ('zngxahi', '0001_initial'),
        ('foijx', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aehywz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hqjnudya', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Afoportru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xpclstuza', models.OneToOneField(null=True, related_name='+', to='foijx.Gsdqrijpp')),
            ],
        ),
        migrations.CreateModel(
            name='Aqqpzvuoxj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elbxadh', models.CharField(default='', max_length=66)),
            ],
        ),
        migrations.CreateModel(
            name='Fmrensoxi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdnkbk', models.ForeignKey(null=True, related_name='+', to='zngxahi.Eauslyif')),
            ],
        ),
        migrations.CreateModel(
            name='Nenfvguk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arptb', models.CharField(default='', max_length=168)),
            ],
        ),
        migrations.CreateModel(
            name='Nrnexasxp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('htfway', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rwrraj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wxbvqnfu', models.OneToOneField(null=True, related_name='+', to='wawqcpvrz.Scfuekgkl')),
            ],
        ),
        migrations.CreateModel(
            name='Ryzutjmqc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oeuvyy', models.CharField(default='', max_length=67)),
            ],
        ),
        migrations.CreateModel(
            name='Zhsexma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cskzi', models.OneToOneField(null=True, related_name='+', to='rrmdjc.Guhhjm')),
            ],
        ),
    ]
