# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glcmkwkzv', '0001_initial'),
        ('wulegwfs', '0001_initial'),
        ('foijx', '0002_auto_20150218_1621'),
        ('ruvaymw', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bdontoyqti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmctlsx', models.ForeignKey(null=True, related_name='+', to='ruvaymw.Swanlanqxn')),
            ],
        ),
        migrations.CreateModel(
            name='Eauslyif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ryfajv', models.ForeignKey(null=True, related_name='+', to='glcmkwkzv.Iwzqe')),
            ],
        ),
        migrations.CreateModel(
            name='Hiqedajgiu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpbwjagjg', models.CharField(default='', max_length=253)),
            ],
        ),
        migrations.CreateModel(
            name='Kbgdzldxz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jdhsjo', models.CharField(default='', max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Llnksobygh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xjfzzpp', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Nnkqr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xgosa', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Nxqpxgzt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fwhyytck', models.CharField(default='', max_length=216)),
            ],
        ),
        migrations.CreateModel(
            name='Qahkfonewx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdxgci', models.ForeignKey(null=True, related_name='+', to='wulegwfs.Yxsnty')),
            ],
        ),
        migrations.CreateModel(
            name='Rxxpitmckt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mytzcfoeq', models.ForeignKey(null=True, related_name='+', to='foijx.Qrwsj')),
            ],
        ),
        migrations.CreateModel(
            name='Xrrtgf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twchfjwyg', models.IntegerField(default=0)),
            ],
        ),
    ]
