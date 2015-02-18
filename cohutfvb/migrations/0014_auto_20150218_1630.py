# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakry', '0015_auto_20150218_1630'),
        ('cohutfvb', '0013_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecgjvad',
            name='dmlqug',
        ),
        migrations.AddField(
            model_name='ecgjvad',
            name='xoyasniyf',
            field=models.OneToOneField(null=True, related_name='+', to='kakry.Xgsseizbpr'),
        ),
    ]
