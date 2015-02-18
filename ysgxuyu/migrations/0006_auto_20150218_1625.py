# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohutfvb', '0010_remove_qpuji_pozefnkorz'),
        ('ysgxuyu', '0005_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='omtmse',
            name='ipywv',
        ),
        migrations.AddField(
            model_name='omtmse',
            name='ozlgxphz',
            field=models.OneToOneField(null=True, related_name='+', to='cohutfvb.Qpuji'),
        ),
    ]
