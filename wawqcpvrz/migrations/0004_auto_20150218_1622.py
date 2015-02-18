# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kfapsax', '0002_auto_20150218_1621'),
        ('wawqcpvrz', '0003_scfuekgkl_rhgqd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ndmxpw',
            name='narpapscx',
        ),
        migrations.RemoveField(
            model_name='nrmckl',
            name='yrmez',
        ),
        migrations.AddField(
            model_name='ndmxpw',
            name='njspsh',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='nrmckl',
            name='esgced',
            field=models.CharField(default='', max_length=207),
        ),
        migrations.AddField(
            model_name='xivomw',
            name='kjnag',
            field=models.OneToOneField(null=True, related_name='+', to='kfapsax.Kmwzcb'),
        ),
    ]
