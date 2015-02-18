# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glcmkwkzv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Txgqxz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tthzcisvp', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Yxsnty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qhjcri', models.ForeignKey(null=True, related_name='+', to='glcmkwkzv.Iwzqe')),
            ],
        ),
    ]
