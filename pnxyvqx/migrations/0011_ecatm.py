# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnxyvqx', '0010_auto_20150218_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ecatm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kbkjjed', models.CharField(default='', max_length=202)),
            ],
        ),
    ]
