# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcyjx', '0001_initial'),
        ('gtfgy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bwnmpizji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ryght', models.OneToOneField(null=True, related_name='+', to='gcyjx.Snjsz')),
            ],
        ),
        migrations.CreateModel(
            name='Ddzxkrvtfd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pgrnuiuqmv', models.CharField(default='', max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Guhhjm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ehzyfcfm', models.OneToOneField(null=True, related_name='+', to='rrmdjc.Ddzxkrvtfd')),
            ],
        ),
        migrations.CreateModel(
            name='Gxoqulk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cimezoiy', models.OneToOneField(null=True, related_name='+', to='gtfgy.Swasd')),
            ],
        ),
        migrations.CreateModel(
            name='Rtbkg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eoticlded', models.CharField(default='', max_length=183)),
            ],
        ),
    ]
