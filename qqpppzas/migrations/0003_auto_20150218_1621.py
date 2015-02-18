# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bniworfy', '0005_auto_20150218_1621'),
        ('qqpppzas', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tqlaa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zezpryllj', models.OneToOneField(null=True, related_name='+', to='bniworfy.Sbfynkpvu')),
            ],
        ),
        migrations.RemoveField(
            model_name='mukbde',
            name='laticxbs',
        ),
    ]
