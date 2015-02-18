# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0004_auto_20150218_1621'),
        ('ruvaymw', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zpubci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mvnkwqm', models.ForeignKey(null=True, related_name='+', to='foijx.Qrwsj')),
            ],
        ),
        migrations.RemoveField(
            model_name='ndhcup',
            name='zqxzb',
        ),
        migrations.RemoveField(
            model_name='wmifd',
            name='yalhscl',
        ),
        migrations.AddField(
            model_name='ndhcup',
            name='tqkbptpb',
            field=models.CharField(default='', max_length=139),
        ),
        migrations.AddField(
            model_name='wmifd',
            name='vyposv',
            field=models.IntegerField(default=0),
        ),
    ]
