# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digmcd', '0006_auto_20150218_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Krbaxhjpkp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jqqic', models.ForeignKey(null=True, related_name='+', to='digmcd.Krbaxhjpkp')),
            ],
        ),
        migrations.AddField(
            model_name='xovte',
            name='rsvwhn',
            field=models.IntegerField(default=0),
        ),
    ]
