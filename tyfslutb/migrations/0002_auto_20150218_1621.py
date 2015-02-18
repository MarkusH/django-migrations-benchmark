# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygnakzgjxu', '0001_initial'),
        ('tyfslutb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ckvpx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtnnovz', models.OneToOneField(null=True, related_name='+', to='ygnakzgjxu.Mxlpodxpm')),
            ],
        ),
        migrations.RemoveField(
            model_name='ynbpgqn',
            name='udhaejrfhb',
        ),
    ]
