# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyfslutb', '0006_ynbpgqn_pgbxqxfrn'),
        ('ladqux', '0003_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fqhqdv',
            name='ubybounu',
        ),
        migrations.AddField(
            model_name='fqhqdv',
            name='ukqyakhyd',
            field=models.ForeignKey(null=True, related_name='+', to='tyfslutb.Juemb'),
        ),
        migrations.AddField(
            model_name='oeyhu',
            name='skcbskaz',
            field=models.IntegerField(default=0),
        ),
    ]
