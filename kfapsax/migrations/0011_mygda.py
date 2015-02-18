# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0019_auto_20150218_1631'),
        ('kfapsax', '0010_zvpuolsnx_ypflrrmma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mygda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csipywcnvu', models.OneToOneField(null=True, related_name='+', to='zhavbmq.Ybkewg')),
            ],
        ),
    ]
