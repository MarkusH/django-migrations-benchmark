# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkfudme', '0008_auto_20150218_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qhsnzq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttkgebv', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='dbpile',
            name='ynyiuist',
        ),
        migrations.AddField(
            model_name='dbpile',
            name='iqimpcc',
            field=models.CharField(default='', max_length=99),
        ),
        migrations.AddField(
            model_name='ewxxluebq',
            name='agnkvhewuf',
            field=models.CharField(default='', max_length=153),
        ),
    ]
