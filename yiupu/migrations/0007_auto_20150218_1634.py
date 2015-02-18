# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcyjx', '0013_remove_xdvbgtxz_bdkdii'),
        ('yiupu', '0006_khayviiua'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='khayviiua',
            name='fmuidqqdq',
        ),
        migrations.AddField(
            model_name='khayviiua',
            name='ioudnxgvn',
            field=models.OneToOneField(null=True, related_name='+', to='gcyjx.Xdvbgtxz'),
        ),
    ]
