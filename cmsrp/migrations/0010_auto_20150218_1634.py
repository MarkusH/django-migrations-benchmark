# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsrp', '0009_auto_20150218_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rkknf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uojzx', models.CharField(default='', max_length=203)),
            ],
        ),
        migrations.RemoveField(
            model_name='bovkv',
            name='yzohilanvo',
        ),
        migrations.DeleteModel(
            name='Bovkv',
        ),
    ]
