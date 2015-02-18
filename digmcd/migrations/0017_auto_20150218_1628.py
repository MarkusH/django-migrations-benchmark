# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuspknbh', '0015_auto_20150218_1628'),
        ('avwpufexob', '0013_auto_20150218_1628'),
        ('digmcd', '0016_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yymzlvsz',
            name='apkorgjb',
        ),
        migrations.RemoveField(
            model_name='zaganduq',
            name='lxkoptjj',
        ),
        migrations.AddField(
            model_name='krbaxhjpkp',
            name='pgyav',
            field=models.OneToOneField(null=True, related_name='+', to='avwpufexob.Aunuwoo'),
        ),
        migrations.AddField(
            model_name='mqnavvvb',
            name='akttuw',
            field=models.OneToOneField(null=True, related_name='+', to='cuspknbh.Mwigq'),
        ),
    ]
