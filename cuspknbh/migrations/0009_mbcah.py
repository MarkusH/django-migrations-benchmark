# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohutfvb', '0009_auto_20150218_1623'),
        ('cuspknbh', '0008_auto_20150218_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mbcah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddbfeooid', models.ForeignKey(null=True, related_name='+', to='cohutfvb.Crzqih')),
            ],
        ),
    ]
