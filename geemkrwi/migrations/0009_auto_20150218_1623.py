# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geemkrwi', '0008_remove_wilsmoea_xguaklb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hxkigetost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vixlvfvme', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='mxvmqmhku',
            name='lumaqoyepr',
        ),
        migrations.AddField(
            model_name='egvtran',
            name='tcqukiomh',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mxvmqmhku',
            name='ioauv',
            field=models.CharField(default='', max_length=102),
        ),
    ]
