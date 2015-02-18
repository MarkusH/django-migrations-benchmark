# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bniworfy', '0017_auto_20150218_1632'),
        ('khwbgr', '0009_auto_20150218_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ibuazau',
            name='edfxe',
        ),
        migrations.AddField(
            model_name='ibuazau',
            name='pssnb',
            field=models.OneToOneField(null=True, related_name='+', to='bniworfy.Trjyk'),
        ),
    ]
