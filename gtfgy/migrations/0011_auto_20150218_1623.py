# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtfgy', '0010_auto_20150218_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symqs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zdbraaw', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='rykamine',
            name='ueuzllk',
        ),
        migrations.AddField(
            model_name='niwaoqfft',
            name='scqnrmm',
            field=models.CharField(default='', max_length=126),
        ),
        migrations.AddField(
            model_name='rykamine',
            name='iacoapjau',
            field=models.CharField(default='', max_length=51),
        ),
    ]
