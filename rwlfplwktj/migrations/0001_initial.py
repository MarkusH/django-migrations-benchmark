# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Knoeepjnhs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('azutzivj', models.OneToOneField(null=True, related_name='+', to='zhavbmq.Ohfvuo')),
            ],
        ),
    ]
