# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wawqcpvrz', '0007_auto_20150218_1623'),
        ('ruvaymw', '0012_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hhnwphllci',
            name='wmriml',
        ),
        migrations.AddField(
            model_name='wmifd',
            name='rvygrr',
            field=models.OneToOneField(null=True, related_name='+', to='wawqcpvrz.Xivomw'),
        ),
    ]
