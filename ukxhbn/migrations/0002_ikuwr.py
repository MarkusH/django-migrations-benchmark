# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qqpppzas', '0002_auto_20150218_1621'),
        ('ukxhbn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ikuwr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vmxtci', models.OneToOneField(null=True, related_name='+', to='qqpppzas.Mukbde')),
            ],
        ),
    ]
