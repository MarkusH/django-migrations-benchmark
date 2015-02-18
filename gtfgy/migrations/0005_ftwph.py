# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruvaymw', '0003_auto_20150218_1621'),
        ('gtfgy', '0004_auto_20150218_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ftwph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gatahehq', models.OneToOneField(null=True, related_name='+', to='ruvaymw.Swanlanqxn')),
            ],
        ),
    ]
