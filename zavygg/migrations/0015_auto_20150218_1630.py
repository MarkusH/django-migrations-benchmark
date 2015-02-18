# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavygg', '0014_remove_jydvnf_xwilqwztoj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gbmslrhm',
            name='wftcam',
        ),
        migrations.AddField(
            model_name='gbmslrhm',
            name='ezrgxhh',
            field=models.IntegerField(default=0),
        ),
    ]
