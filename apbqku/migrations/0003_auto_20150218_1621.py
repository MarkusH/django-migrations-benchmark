# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apbqku', '0002_ssgsglh_yihuniyqgd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klgmvpd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ydxtalwb', models.CharField(default='', max_length=72)),
            ],
        ),
        migrations.RemoveField(
            model_name='ssgsglh',
            name='yihuniyqgd',
        ),
        migrations.AddField(
            model_name='ssgsglh',
            name='mochrw',
            field=models.CharField(default='', max_length=9),
        ),
    ]
