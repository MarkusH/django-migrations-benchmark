# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuspknbh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ivcsuscyb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lypce', models.ForeignKey(null=True, related_name='+', to='cuspknbh.Kekzfmudvr')),
            ],
        ),
        migrations.CreateModel(
            name='Snjsz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uxkarnxudp', models.CharField(default='', max_length=136)),
            ],
        ),
    ]
