# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burhjvc', '0006_auto_20150218_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jnyynhgbb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kasrh', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='bewsptdyqv',
            name='mcxzdt',
        ),
        migrations.AddField(
            model_name='bewsptdyqv',
            name='xeqlaepw',
            field=models.IntegerField(default=0),
        ),
    ]
