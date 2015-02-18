# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyxbcga', '0007_kpjlirt_uqfzpsgjj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='begquxerkm',
            name='hyfisaxclk',
        ),
        migrations.RemoveField(
            model_name='eezxvbbvmn',
            name='pvonh',
        ),
        migrations.RemoveField(
            model_name='qqpfvbjbpk',
            name='ciomneaa',
        ),
        migrations.AddField(
            model_name='begquxerkm',
            name='eyasqv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='eezxvbbvmn',
            name='cjiikmfzn',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qqpfvbjbpk',
            name='wpljiemmbt',
            field=models.CharField(default='', max_length=77),
        ),
    ]
