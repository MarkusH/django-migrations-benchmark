# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burhjvc', '0007_auto_20150218_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qwtnucajp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdyln', models.CharField(default='', max_length=103)),
            ],
        ),
        migrations.RemoveField(
            model_name='qbuqivoko',
            name='mdvtre',
        ),
    ]
