# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rqwywo', '0008_auto_20150218_1625'),
        ('rwlfplwktj', '0006_auto_20150218_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yjzzdopc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eeagp', models.ForeignKey(null=True, related_name='+', to='rqwywo.Gkiwtx')),
            ],
        ),
    ]
