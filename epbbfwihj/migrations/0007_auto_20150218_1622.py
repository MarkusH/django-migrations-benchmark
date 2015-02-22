# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geemkrwi', '0007_auto_20150218_1622'),
        ('epbbfwihj', '0006_auto_20150218_1622'),
    ]

    run_before = [
        ('khwbgr', '0006_auto_20150218_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wcklq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pgnrf', models.ForeignKey(null=True, related_name='+', to='geemkrwi.Uqqgcprwn')),
            ],
        ),
        migrations.RemoveField(
            model_name='pbnaktpzhs',
            name='vxycehzcf',
        ),
        migrations.RemoveField(
            model_name='uwaayy',
            name='ymklbmt',
        ),
        migrations.RemoveField(
            model_name='zfpgchkbaz',
            name='zgdobd',
        ),
        migrations.DeleteModel(
            name='Pbnaktpzhs',
        ),
    ]
