# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esznwrr', '0001_initial'),
        ('qclaxc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hcetattb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('njfdgh', models.OneToOneField(null=True, related_name='+', to='qclaxc.Ooecads')),
            ],
        ),
        migrations.CreateModel(
            name='Inyvz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nqrrfjy', models.ForeignKey(null=True, related_name='+', to='esznwrr.Cepov')),
            ],
        ),
    ]
