# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khwbgr', '0005_ywojvtbwa_poqdx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bwshcnprcg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pxxuuwa', models.CharField(default='', max_length=93)),
            ],
        ),
        migrations.RemoveField(
            model_name='ywojvtbwa',
            name='evkjp',
        ),
        migrations.RemoveField(
            model_name='ywojvtbwa',
            name='poqdx',
        ),
        migrations.DeleteModel(
            name='Ywojvtbwa',
        ),
    ]
