# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcyjx', '0010_auto_20150218_1626'),
        ('khwbgr', '0006_auto_20150218_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ibuazau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uutjmgjxmy', models.OneToOneField(null=True, related_name='+', to='gcyjx.Nmbztrlh')),
            ],
        ),
        migrations.DeleteModel(
            name='Bwshcnprcg',
        ),
    ]
