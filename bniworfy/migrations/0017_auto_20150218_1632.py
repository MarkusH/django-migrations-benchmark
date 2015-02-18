# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epbbfwihj', '0016_dfjxgqll'),
        ('bniworfy', '0016_auto_20150218_1631'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sbfynkpvu',
        ),
        migrations.RemoveField(
            model_name='kjwyneff',
            name='zctecjt',
        ),
        migrations.AddField(
            model_name='kjwyneff',
            name='mhupwxf',
            field=models.OneToOneField(null=True, related_name='+', to='epbbfwihj.Sysnlv'),
        ),
    ]
