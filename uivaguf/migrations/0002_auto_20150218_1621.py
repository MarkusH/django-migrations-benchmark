# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kfapsax', '0001_initial'),
        ('mjdxvqk', '0003_waktrjgi'),
        ('uivaguf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bqjxljlwq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veqvxofwt', models.ForeignKey(null=True, related_name='+', to='mjdxvqk.Edugsywcj')),
            ],
        ),
        migrations.RemoveField(
            model_name='zwjgfcdi',
            name='gwxtnqawxt',
        ),
        migrations.AddField(
            model_name='zwjgfcdi',
            name='ymtyj',
            field=models.ForeignKey(null=True, related_name='+', to='kfapsax.Sehvi'),
        ),
    ]
