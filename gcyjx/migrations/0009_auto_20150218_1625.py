# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruvaymw', '0012_auto_20150218_1625'),
        ('gcyjx', '0008_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snjsz',
            name='vtafuxd',
        ),
        migrations.AddField(
            model_name='snjsz',
            name='qsntdomu',
            field=models.ForeignKey(null=True, related_name='+', to='ruvaymw.Faqagt'),
        ),
    ]
