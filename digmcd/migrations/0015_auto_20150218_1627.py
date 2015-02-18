# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtfgy', '0016_auto_20150218_1627'),
        ('digmcd', '0014_auto_20150218_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mqnavvvb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cvopda', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='yymzlvsz',
            name='apkorgjb',
            field=models.OneToOneField(null=True, related_name='+', to='gtfgy.Wnhvelxdeb'),
        ),
    ]
