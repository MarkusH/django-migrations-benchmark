# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joavhqi', '0006_pqetbg'),
        ('yiupu', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zzsheqzf',
            name='tdlqispdp',
        ),
        migrations.AddField(
            model_name='zzsheqzf',
            name='lknqwuwtwt',
            field=models.ForeignKey(null=True, related_name='+', to='joavhqi.Lfssmpr'),
        ),
    ]
