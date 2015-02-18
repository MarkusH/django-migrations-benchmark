# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etnevwmkj', '0010_auto_20150218_1628'),
        ('digmcd', '0017_auto_20150218_1628'),
        ('zngxahi', '0015_auto_20150218_1628'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Llnksobygh',
        ),
        migrations.RemoveField(
            model_name='eauslyif',
            name='uosdpbua',
        ),
        migrations.AddField(
            model_name='bdontoyqti',
            name='wtqko',
            field=models.ForeignKey(null=True, related_name='+', to='digmcd.Yymzlvsz'),
        ),
        migrations.AddField(
            model_name='eauslyif',
            name='zzadgnvsif',
            field=models.OneToOneField(null=True, related_name='+', to='etnevwmkj.Ryfwmkefy'),
        ),
    ]
