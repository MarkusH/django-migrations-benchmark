# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygnakzgjxu', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xpmnn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qhdmcyw', models.CharField(default='', max_length=24)),
            ],
        ),
        migrations.DeleteModel(
            name='Sroqtodsnf',
        ),
    ]
