# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcfrcnas', '0003_iwhkq_bqlssqo'),
    ]

    run_before = [
        ('yiupu', '0002_delete_jpmwh'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Snszfzibo',
        ),
        migrations.RemoveField(
            model_name='qibygpddzw',
            name='hachwpnpia',
        ),
        migrations.AddField(
            model_name='ncptyh',
            name='pehkutt',
            field=models.IntegerField(default=0),
        ),
    ]
