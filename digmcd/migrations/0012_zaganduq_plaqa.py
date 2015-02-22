# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esznwrr', '0003_remove_cepov_nwbxduzb'),
        ('digmcd', '0011_auto_20150218_1623'),
    ]

    run_before = [
        ('esznwrr', '0004_delete_vppjpa'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaganduq',
            name='plaqa',
            field=models.ForeignKey(null=True, related_name='+', to='esznwrr.Vppjpa'),
        ),
    ]
