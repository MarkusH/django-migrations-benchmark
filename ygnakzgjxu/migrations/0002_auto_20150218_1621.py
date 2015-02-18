# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygnakzgjxu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sroqtodsnf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('znrovzwq', models.CharField(default='', max_length=175)),
            ],
        ),
        migrations.RemoveField(
            model_name='mxlpodxpm',
            name='jfzctxqsbj',
        ),
        migrations.DeleteModel(
            name='Mxlpodxpm',
        ),
    ]
