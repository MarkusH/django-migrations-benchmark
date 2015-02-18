# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0001_initial'),
        ('cohutfvb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kmwzcb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zahlcf', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ktjsrtd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dauxp', models.ForeignKey(null=True, related_name='+', to='cohutfvb.Qpuji')),
            ],
        ),
        migrations.CreateModel(
            name='Sehvi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wspsk', models.OneToOneField(null=True, related_name='+', to='foijx.Wrafoshzom')),
            ],
        ),
    ]
