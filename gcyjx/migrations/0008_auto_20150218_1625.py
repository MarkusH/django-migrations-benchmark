# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcyjx', '0007_auto_20150218_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snjsz',
            name='vyrxggwcrm',
        ),
        migrations.AddField(
            model_name='snjsz',
            name='vtafuxd',
            field=models.CharField(default='', max_length=237),
        ),
    ]
