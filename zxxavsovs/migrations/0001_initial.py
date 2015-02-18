# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esznwrr', '0001_initial'),
        ('mjdxvqk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fiellmltob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xpmob', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hhmcp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Iyfiu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('druuyy', models.OneToOneField(null=True, related_name='+', to='mjdxvqk.Ovbcnxcwyr')),
            ],
        ),
        migrations.CreateModel(
            name='Kiikphbz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wtcqvpcl', models.OneToOneField(null=True, related_name='+', to='esznwrr.Vppjpa')),
            ],
        ),
        migrations.CreateModel(
            name='Yjuyutcqq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fxutowlcpb', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='hhmcp',
            name='ruddjkf',
            field=models.ForeignKey(null=True, related_name='+', to='zxxavsovs.Yjuyutcqq'),
        ),
    ]
