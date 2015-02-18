# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khwbgr', '0008_auto_20150218_1627'),
        ('kfapsax', '0008_auto_20150218_1627'),
        ('rqwywo', '0009_jsvynw'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rrojp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saknhbe', models.ForeignKey(null=True, related_name='+', to='kfapsax.Zvpuolsnx')),
            ],
        ),
        migrations.RemoveField(
            model_name='jsvynw',
            name='crogp',
        ),
        migrations.AddField(
            model_name='jsvynw',
            name='cznktgglif',
            field=models.ForeignKey(null=True, related_name='+', to='khwbgr.Ibuazau'),
        ),
    ]
