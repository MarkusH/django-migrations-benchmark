# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qclaxc', '0012_auto_20150218_1626'),
        ('bniworfy', '0012_auto_20150218_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='kjwyneff',
            name='recvtzi',
            field=models.CharField(default='', max_length=119),
        ),
        migrations.AddField(
            model_name='vnjcuelh',
            name='gjymbyzq',
            field=models.OneToOneField(null=True, related_name='+', to='qclaxc.Ooecads'),
        ),
    ]
