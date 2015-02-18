# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuspknbh', '0005_auto_20150218_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yicalotegs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yhkzxndlz', models.IntegerField(default=0)),
            ],
        ),
    ]
