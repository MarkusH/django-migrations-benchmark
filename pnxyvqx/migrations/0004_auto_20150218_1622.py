# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakry', '0006_auto_20150218_1622'),
        ('pnxyvqx', '0003_delete_aqqpzvuoxj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='afoportru',
            name='xpclstuza',
        ),
        migrations.RemoveField(
            model_name='nrnexasxp',
            name='dzshhvc',
        ),
        migrations.RemoveField(
            model_name='rwrraj',
            name='wxbvqnfu',
        ),
        migrations.AddField(
            model_name='rwrraj',
            name='qcbtpghkq',
            field=models.ForeignKey(null=True, related_name='+', to='kakry.Ajbkovws'),
        ),
        migrations.DeleteModel(
            name='Afoportru',
        ),
    ]
