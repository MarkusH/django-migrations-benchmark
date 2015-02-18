# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kfapsax', '0001_initial'),
        ('mntrwrm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xevahddk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vxckqc', models.ForeignKey(null=True, related_name='+', to='kfapsax.Sehvi')),
            ],
        ),
    ]
