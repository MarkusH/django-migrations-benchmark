# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zsskgviadw', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ylpjiaq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yxrkt', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='ltlsozji',
            name='fzlko',
        ),
        migrations.AddField(
            model_name='ltlsozji',
            name='nhiafkfonb',
            field=models.CharField(default='', max_length=86),
        ),
    ]
