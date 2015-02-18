# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digmcd', '0001_initial'),
        ('khwbgr', '0001_initial'),
        ('burhjvc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ydprem',
            name='npbbb',
            field=models.OneToOneField(null=True, related_name='+', to='khwbgr.Fetzvwamur'),
        ),
        migrations.AddField(
            model_name='qbuqivoko',
            name='mdvtre',
            field=models.OneToOneField(null=True, related_name='+', to='digmcd.Xmvhvzui'),
        ),
    ]
