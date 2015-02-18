# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wawqcpvrz', '0002_delete_vrvslusmy'),
        ('ruvaymw', '0002_auto_20150218_1621'),
        ('foijx', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abmhnczd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wdlblsubi', models.OneToOneField(null=True, related_name='+', to='ruvaymw.Bdpibttuxi')),
            ],
        ),
        migrations.AddField(
            model_name='mvmwqukrbx',
            name='ynlaiak',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wrafoshzom',
            name='qqpfdtng',
            field=models.ForeignKey(null=True, related_name='+', to='wawqcpvrz.Ydfkef'),
        ),
    ]
