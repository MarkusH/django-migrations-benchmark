# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geemkrwi', '0019_dscegsanff'),
        ('rrmdjc', '0010_auto_20150218_1632'),
        ('gbsaqmaxu', '0019_delete_vvyni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vqtzjsu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnmqsqv', models.ForeignKey(null=True, related_name='+', to='rrmdjc.Guhhjm')),
            ],
        ),
        migrations.RemoveField(
            model_name='nzleswyp',
            name='cfvih',
        ),
        migrations.AddField(
            model_name='nhlpe',
            name='reoabc',
            field=models.CharField(default='', max_length=198),
        ),
        migrations.AddField(
            model_name='nzleswyp',
            name='gbyvc',
            field=models.OneToOneField(null=True, related_name='+', to='geemkrwi.Mxvmqmhku'),
        ),
    ]
