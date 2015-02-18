# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygnakzgjxu', '0007_auto_20150218_1623'),
        ('wyxbcga', '0010_auto_20150218_1625'),
        ('qqpppzas', '0011_auto_20150218_1625'),
        ('gbsaqmaxu', '0011_knqau_ytwbrbx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rkmtigdh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yowznhii', models.ForeignKey(null=True, related_name='+', to='wyxbcga.Xqjugixefj')),
            ],
        ),
        migrations.RemoveField(
            model_name='lshmrghvzw',
            name='iqdetwvwf',
        ),
        migrations.RemoveField(
            model_name='lshmrghvzw',
            name='olicbgstaw',
        ),
        migrations.RemoveField(
            model_name='nhlpe',
            name='wfetmax',
        ),
        migrations.AddField(
            model_name='avwudusy',
            name='kzgsda',
            field=models.CharField(default='', max_length=229),
        ),
        migrations.AddField(
            model_name='lshmrghvzw',
            name='oodpnzzt',
            field=models.OneToOneField(null=True, related_name='+', to='qqpppzas.Lrqwbz'),
        ),
        migrations.AddField(
            model_name='nhlpe',
            name='mcctecfjs',
            field=models.OneToOneField(null=True, related_name='+', to='ygnakzgjxu.Ttzean'),
        ),
    ]
