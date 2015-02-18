# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0008_auto_20150218_1623'),
        ('bniworfy', '0008_auto_20150218_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dvqne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubeuubhtm', models.CharField(default='', max_length=242)),
            ],
        ),
        migrations.AddField(
            model_name='mxfnrc',
            name='vwngisguf',
            field=models.ForeignKey(null=True, related_name='+', to='zhavbmq.Hmaopvcufb'),
        ),
    ]
