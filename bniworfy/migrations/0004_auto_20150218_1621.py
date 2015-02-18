# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rwlfplwktj', '0001_initial'),
        ('ysgxuyu', '0001_initial'),
        ('ygnakzgjxu', '0001_initial'),
        ('bniworfy', '0003_dkvkm_eylgo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dkvkm',
            name='eylgo',
        ),
        migrations.RemoveField(
            model_name='gsmbfohda',
            name='vuszhgsx',
        ),
        migrations.RemoveField(
            model_name='kjwyneff',
            name='wfujlt',
        ),
        migrations.RemoveField(
            model_name='mxfnrc',
            name='pmqdg',
        ),
        migrations.RemoveField(
            model_name='trjyk',
            name='ngubcf',
        ),
        migrations.AddField(
            model_name='dkvkm',
            name='nteqflev',
            field=models.OneToOneField(null=True, related_name='+', to='ygnakzgjxu.Mxlpodxpm'),
        ),
        migrations.AddField(
            model_name='gsmbfohda',
            name='xtcnijqs',
            field=models.ForeignKey(null=True, related_name='+', to='ysgxuyu.Kqlunbkaa'),
        ),
        migrations.AddField(
            model_name='kjwyneff',
            name='zctecjt',
            field=models.CharField(default='', max_length=62),
        ),
        migrations.AddField(
            model_name='mxfnrc',
            name='ifxub',
            field=models.OneToOneField(null=True, related_name='+', to='rwlfplwktj.Knoeepjnhs'),
        ),
        migrations.AddField(
            model_name='trjyk',
            name='durndkeais',
            field=models.CharField(default='', max_length=159),
        ),
    ]
