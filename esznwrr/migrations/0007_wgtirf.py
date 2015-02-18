# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irmtbds', '0010_auto_20150218_1632'),
        ('esznwrr', '0006_tbxjbiqnck'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wgtirf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ulpzex', models.ForeignKey(null=True, related_name='+', to='irmtbds.Rqikftw')),
            ],
        ),
    ]
