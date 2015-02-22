# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emncdxt', '0004_auto_20150218_1621'),
        ('zhavbmq', '0004_hmaopvcufb_vabnk'),
    ]

    run_before = [
        ('irmtbds', '0004_auto_20150218_1622'),
        ('avwpufexob', '0006_auto_20150218_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Murrsbmz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lsdctjp', models.OneToOneField(null=True, related_name='+', to='emncdxt.Mioxdvg')),
            ],
        ),
        migrations.RemoveField(
            model_name='hmaopvcufb',
            name='infpgx',
        ),
        migrations.RemoveField(
            model_name='hmaopvcufb',
            name='vabnk',
        ),
    ]
