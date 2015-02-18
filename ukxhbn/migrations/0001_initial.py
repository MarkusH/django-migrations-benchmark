# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zsskgviadw', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dcphul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aschcos', models.ForeignKey(null=True, related_name='+', to='zsskgviadw.Hcetattb')),
            ],
        ),
        migrations.CreateModel(
            name='Xtmekz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lvvzn', models.IntegerField(default=0)),
            ],
        ),
    ]
