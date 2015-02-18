# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esznwrr', '0001_initial'),
        ('digmcd', '0001_initial'),
        ('apbqku', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Onmti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vcevpdll', models.OneToOneField(null=True, related_name='+', to='apbqku.Ssgsglh')),
            ],
        ),
        migrations.CreateModel(
            name='Opwgwxncp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kxmfnvxfoi', models.OneToOneField(null=True, related_name='+', to='esznwrr.Vppjpa')),
            ],
        ),
        migrations.CreateModel(
            name='Ubuhm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qbjla', models.ForeignKey(null=True, related_name='+', to='apbqku.Ffussl')),
            ],
        ),
        migrations.CreateModel(
            name='Vqykzihlmk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bpxwllwdt', models.ForeignKey(null=True, related_name='+', to='digmcd.Xovte')),
            ],
        ),
        migrations.CreateModel(
            name='Zwjgfcdi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gwxtnqawxt', models.IntegerField(default=0)),
            ],
        ),
    ]
