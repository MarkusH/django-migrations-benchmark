# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakry', '0013_auto_20150218_1627'),
        ('gbsaqmaxu', '0013_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lshmrghvzw',
            name='oodpnzzt',
        ),
        migrations.AddField(
            model_name='avwudusy',
            name='fctsrubu',
            field=models.OneToOneField(null=True, related_name='+', to='kakry.Kiurw'),
        ),
        migrations.AddField(
            model_name='nhlpe',
            name='imicowhnou',
            field=models.CharField(default='', max_length=209),
        ),
        migrations.DeleteModel(
            name='Lshmrghvzw',
        ),
    ]
