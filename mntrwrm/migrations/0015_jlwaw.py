# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mntrwrm', '0014_delete_xevahddk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jlwaw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mqhumi', models.CharField(default='', max_length=69)),
            ],
        ),
    ]
