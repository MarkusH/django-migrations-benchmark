# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygnakzgjxu', '0008_auto_20150218_1626'),
        ('tyfslutb', '0014_auto_20150218_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bmzhg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nlcvjjxtmx', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='qcwbo',
            name='helryvwow',
            field=models.OneToOneField(null=True, related_name='+', to='ygnakzgjxu.Xdwhlpqgw'),
        ),
        migrations.AddField(
            model_name='ynbpgqn',
            name='dxemnqzz',
            field=models.CharField(default='', max_length=208),
        ),
    ]
