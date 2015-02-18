# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khwbgr', '0009_auto_20150218_1630'),
        ('geemkrwi', '0016_auto_20150218_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wilsmoea',
            name='lpmmn',
        ),
        migrations.AddField(
            model_name='wilsmoea',
            name='colpvkh',
            field=models.OneToOneField(null=True, related_name='+', to='khwbgr.Ibuazau'),
        ),
    ]
