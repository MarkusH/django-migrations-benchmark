# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyfslutb', '0009_auto_20150218_1623'),
        ('mntrwrm', '0006_auto_20150218_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='eaeehqi',
            name='stfgtnuej',
            field=models.OneToOneField(null=True, related_name='+', to='tyfslutb.Qcwbo'),
        ),
    ]
