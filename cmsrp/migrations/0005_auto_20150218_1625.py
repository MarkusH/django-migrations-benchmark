# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsrp', '0004_remove_ncysy_lkvgwwfoan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miakjx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tqwbvjcjda', models.CharField(default='', max_length=196)),
            ],
        ),
        migrations.DeleteModel(
            name='Ncysy',
        ),
    ]
