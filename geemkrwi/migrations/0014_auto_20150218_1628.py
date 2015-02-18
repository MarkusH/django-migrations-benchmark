# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avwpufexob', '0013_auto_20150218_1628'),
        ('geemkrwi', '0013_wilsmoea_lpmmn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Knrrd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgykwsrkc', models.ForeignKey(null=True, related_name='+', to='avwpufexob.Fvlkcjd')),
            ],
        ),
        migrations.RemoveField(
            model_name='hxkigetost',
            name='ycqitjgln',
        ),
        migrations.RemoveField(
            model_name='mxvtxbqsa',
            name='ipxqzrwy',
        ),
        migrations.AddField(
            model_name='hxkigetost',
            name='egtpieu',
            field=models.CharField(default='', max_length=50),
        ),
    ]
