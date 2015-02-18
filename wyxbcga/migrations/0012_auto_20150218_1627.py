# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irmtbds', '0008_auto_20150218_1627'),
        ('wyxbcga', '0011_auto_20150218_1626'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Kpjlirt',
        ),
        migrations.RemoveField(
            model_name='begquxerkm',
            name='eyasqv',
        ),
        migrations.RemoveField(
            model_name='eezxvbbvmn',
            name='pvzewhwow',
        ),
        migrations.RemoveField(
            model_name='qqpfvbjbpk',
            name='wpljiemmbt',
        ),
        migrations.AddField(
            model_name='begquxerkm',
            name='uxdnq',
            field=models.OneToOneField(null=True, related_name='+', to='irmtbds.Rqikftw'),
        ),
        migrations.AddField(
            model_name='eezxvbbvmn',
            name='djydzcqxu',
            field=models.CharField(default='', max_length=141),
        ),
        migrations.AddField(
            model_name='qqpfvbjbpk',
            name='ebcai',
            field=models.IntegerField(default=0),
        ),
    ]
