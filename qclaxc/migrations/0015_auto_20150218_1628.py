# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qclaxc', '0014_auto_20150218_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epikaaneig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lfmymwpdk', models.CharField(default='', max_length=211)),
            ],
        ),
        migrations.DeleteModel(
            name='Pmcbxoetr',
        ),
        migrations.RemoveField(
            model_name='jvoopceqsv',
            name='gzzkivnwgi',
        ),
        migrations.AddField(
            model_name='jvoopceqsv',
            name='unzjnfo',
            field=models.CharField(default='', max_length=28),
        ),
    ]
