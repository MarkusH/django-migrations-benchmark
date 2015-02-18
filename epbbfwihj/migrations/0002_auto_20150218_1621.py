# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gbsaqmaxu', '0001_initial'),
        ('epbbfwihj', '0001_initial'),
        ('qclaxc', '0001_initial'),
        ('ukxhbn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zfpgchkbaz',
            name='yttrt',
            field=models.ForeignKey(null=True, related_name='+', to='ukxhbn.Dcphul'),
        ),
        migrations.AddField(
            model_name='uzdthbetj',
            name='cmzqytyp',
            field=models.OneToOneField(null=True, related_name='+', to='gbsaqmaxu.Avwudusy'),
        ),
        migrations.AddField(
            model_name='uwaayy',
            name='jtpsyn',
            field=models.OneToOneField(null=True, related_name='+', to='qclaxc.Yiifw'),
        ),
        migrations.AddField(
            model_name='pbnaktpzhs',
            name='ixryziwdzn',
            field=models.OneToOneField(null=True, related_name='+', to='qclaxc.Bfnecf'),
        ),
    ]
