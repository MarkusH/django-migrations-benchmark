# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emncdxt', '0012_shgjep_qucvdgncbq'),
        ('zxxavsovs', '0011_auto_20150218_1628'),
    ]

    run_before = [
        ('emncdxt', '0013_delete_shgjep'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kxgenek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rgnvvw', models.ForeignKey(null=True, related_name='+', to='emncdxt.Shgjep')),
            ],
        ),
    ]
