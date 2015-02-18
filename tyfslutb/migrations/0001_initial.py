# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joavhqi', '0001_initial'),
        ('digmcd', '0001_initial'),
        ('yiupu', '0001_initial'),
        ('khwbgr', '0001_initial'),
        ('rrmdjc', '0001_initial'),
        ('glcmkwkzv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Copkdxcnlp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gczeinwy', models.OneToOneField(null=True, related_name='+', to='digmcd.Gxovs')),
            ],
        ),
        migrations.CreateModel(
            name='Cvzmphnk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xhcatgbtsw', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Djnppzsr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fkcwrltrh', models.CharField(default='', max_length=101)),
            ],
        ),
        migrations.CreateModel(
            name='Ihswfvupi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ywstkx', models.ForeignKey(null=True, related_name='+', to='glcmkwkzv.Unnork')),
            ],
        ),
        migrations.CreateModel(
            name='Ixmfsgch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zovmenwqiy', models.ForeignKey(null=True, related_name='+', to='rrmdjc.Bwnmpizji')),
            ],
        ),
        migrations.CreateModel(
            name='Juemb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objhsjj', models.OneToOneField(null=True, related_name='+', to='khwbgr.Fetzvwamur')),
            ],
        ),
        migrations.CreateModel(
            name='Qcwbo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zxzurr', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Qhzppcqwku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xjbinng', models.CharField(default='', max_length=219)),
            ],
        ),
        migrations.CreateModel(
            name='Vzqlh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdeaj', models.ForeignKey(null=True, related_name='+', to='joavhqi.Iowgy')),
            ],
        ),
        migrations.CreateModel(
            name='Ynbpgqn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('udhaejrfhb', models.OneToOneField(null=True, related_name='+', to='yiupu.Jpmwh')),
            ],
        ),
    ]
