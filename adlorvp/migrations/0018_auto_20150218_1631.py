# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnxyvqx', '0013_auto_20150218_1630'),
        ('adlorvp', '0017_auto_20150218_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sxjglqejbx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gvukurady', models.ForeignKey(null=True, related_name='+', to='pnxyvqx.Nenfvguk')),
            ],
        ),
        migrations.RemoveField(
            model_name='afyxxcmzds',
            name='webvuzv',
        ),
        migrations.RemoveField(
            model_name='kmygwyorsi',
            name='qtozzpel',
        ),
        migrations.RemoveField(
            model_name='phrzexgxu',
            name='tmlwb',
        ),
        migrations.AddField(
            model_name='afyxxcmzds',
            name='cpjfffw',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ehcuyeglmi',
            name='pvhsiqtxc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kmygwyorsi',
            name='tkqbttaxyk',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='phrzexgxu',
            name='lwtoe',
            field=models.IntegerField(default=0),
        ),
    ]
