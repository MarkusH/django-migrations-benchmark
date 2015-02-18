# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esznwrr', '0001_initial'),
        ('cmsrp', '0001_initial'),
        ('ruvaymw', '0005_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqagt',
            name='rmxcdcuqei',
        ),
        migrations.RemoveField(
            model_name='wmifd',
            name='vyposv',
        ),
        migrations.AddField(
            model_name='faqagt',
            name='vtnbt',
            field=models.ForeignKey(null=True, related_name='+', to='esznwrr.Vppjpa'),
        ),
        migrations.AddField(
            model_name='ndhcup',
            name='xjpmyjji',
            field=models.CharField(default='', max_length=62),
        ),
        migrations.AddField(
            model_name='wmifd',
            name='ztdwwxnoeo',
            field=models.ForeignKey(null=True, related_name='+', to='cmsrp.Ncysy'),
        ),
    ]
