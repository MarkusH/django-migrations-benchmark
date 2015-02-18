# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcyjx', '0005_xdvbgtxz_bdkdii'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nmbztrlh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widhow', models.OneToOneField(null=True, related_name='+', to='gcyjx.Nmbztrlh')),
            ],
        ),
    ]
