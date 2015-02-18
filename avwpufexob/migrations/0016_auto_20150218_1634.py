# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joavhqi', '0016_auto_20150218_1634'),
        ('avwpufexob', '0015_auto_20150218_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nhpkrhkql',
            name='qilej',
        ),
        migrations.AddField(
            model_name='nhpkrhkql',
            name='vbzqbnyrme',
            field=models.CharField(default='', max_length=39),
        ),
        migrations.AddField(
            model_name='yejdqycpmg',
            name='oyjbjizqf',
            field=models.OneToOneField(null=True, related_name='+', to='joavhqi.Sabdmpl'),
        ),
    ]
