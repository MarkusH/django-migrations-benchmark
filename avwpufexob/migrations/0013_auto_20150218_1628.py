# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcyjx', '0011_nmbztrlh_vrbhetrjgt'),
        ('avwpufexob', '0012_auto_20150218_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vxucuqwa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ufrxpg', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='yejdqycpmg',
            name='daqjy',
        ),
        migrations.AddField(
            model_name='yejdqycpmg',
            name='znlynydhet',
            field=models.OneToOneField(null=True, related_name='+', to='gcyjx.Nmbztrlh'),
        ),
    ]
