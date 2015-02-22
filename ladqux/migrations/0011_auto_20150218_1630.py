# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ladqux', '0010_zhgafcksok_nwofpfncc'),
    ]

    run_before = [
        ('ysgxuyu', '0012_delete_bmovnbnmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iznpghp',
            name='sgafrav',
        ),
        migrations.AddField(
            model_name='iznpghp',
            name='czxbnyva',
            field=models.IntegerField(default=0),
        ),
    ]
