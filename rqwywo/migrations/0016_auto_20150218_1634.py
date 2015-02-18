# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apbqku', '0010_ztmubrfn_uivof'),
        ('rqwywo', '0015_auto_20150218_1632'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Wmvmz',
        ),
        migrations.AddField(
            model_name='gkiwtx',
            name='akbmd',
            field=models.ForeignKey(null=True, related_name='+', to='apbqku.Ztmubrfn'),
        ),
    ]
