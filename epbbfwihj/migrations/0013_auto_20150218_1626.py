# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irmtbds', '0007_remove_rqikftw_sjnjki'),
        ('epbbfwihj', '0012_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wcklq',
            name='pgnrf',
        ),
        migrations.AddField(
            model_name='zfpgchkbaz',
            name='jlias',
            field=models.OneToOneField(null=True, related_name='+', to='irmtbds.Rqikftw'),
        ),
        migrations.DeleteModel(
            name='Wcklq',
        ),
    ]
