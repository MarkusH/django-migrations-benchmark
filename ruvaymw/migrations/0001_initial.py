# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ysgxuyu', '0001_initial'),
        ('cuspknbh', '0002_auto_20150218_1621'),
        ('wawqcpvrz', '0001_initial'),
        ('rrmdjc', '0001_initial'),
        ('mntrwrm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bdpibttuxi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zewgqkdoee', models.ForeignKey(null=True, related_name='+', to='cuspknbh.Mwigq')),
            ],
        ),
        migrations.CreateModel(
            name='Faqagt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rmxcdcuqei', models.CharField(default='', max_length=201)),
            ],
        ),
        migrations.CreateModel(
            name='Fxsiyvw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hdhjlmfrsy', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hhnwphllci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('akuhjv', models.ForeignKey(null=True, related_name='+', to='ysgxuyu.Bmovnbnmed')),
            ],
        ),
        migrations.CreateModel(
            name='Ndhcup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zqxzb', models.CharField(default='', max_length=57)),
            ],
        ),
        migrations.CreateModel(
            name='Ofvsocf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dahouzw', models.OneToOneField(null=True, related_name='+', to='wawqcpvrz.Ydfkef')),
            ],
        ),
        migrations.CreateModel(
            name='Owamswc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ekqpnk', models.CharField(default='', max_length=157)),
            ],
        ),
        migrations.CreateModel(
            name='Swanlanqxn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zeqdyy', models.ForeignKey(null=True, related_name='+', to='mntrwrm.Rbhubw')),
            ],
        ),
        migrations.CreateModel(
            name='Wmifd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctfflurp', models.OneToOneField(null=True, related_name='+', to='rrmdjc.Bwnmpizji')),
            ],
        ),
        migrations.CreateModel(
            name='Ylhrvymeyk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qjehrn', models.CharField(default='', max_length=213)),
            ],
        ),
    ]
