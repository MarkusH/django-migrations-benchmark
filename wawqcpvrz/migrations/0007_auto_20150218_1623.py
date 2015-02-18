# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wawqcpvrz', '0006_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scfuekgkl',
            name='wglslgn',
        ),
        migrations.AddField(
            model_name='scfuekgkl',
            name='fwxxkt',
            field=models.CharField(default='', max_length=56),
        ),
    ]
