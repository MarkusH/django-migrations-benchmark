# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wawqcpvrz', '0007_auto_20150218_1623'),
        ('zavygg', '0008_auto_20150218_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oqyncxevyj',
            name='cqpevou',
        ),
        migrations.AddField(
            model_name='ligxr',
            name='bbftsvxk',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='oqyncxevyj',
            name='jefahexng',
            field=models.OneToOneField(null=True, related_name='+', to='wawqcpvrz.Ndmxpw'),
        ),
    ]
