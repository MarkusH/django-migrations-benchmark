# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zngxahi', '0007_auto_20150218_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qmhypaufcg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lrtkrh', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='nnkqr',
            name='tecbgms',
        ),
    ]
