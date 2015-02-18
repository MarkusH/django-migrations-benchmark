# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mntrwrm', '0008_auto_20150218_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kmvkehkum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zibfm', models.CharField(default='', max_length=228)),
            ],
        ),
        migrations.RemoveField(
            model_name='eaeehqi',
            name='tauahpur',
        ),
        migrations.RemoveField(
            model_name='xevahddk',
            name='aheutab',
        ),
    ]
