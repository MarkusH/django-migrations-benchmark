# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuspknbh', '0017_auto_20150218_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wxhfgo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adgkwj', models.CharField(default='', max_length=67)),
            ],
        ),
    ]
