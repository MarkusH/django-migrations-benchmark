# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ysgxuyu', '0005_auto_20150218_1622'),
        ('rwlfplwktj', '0002_knoeepjnhs_kluyzayvh'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xunyyu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haaxfgcmii', models.OneToOneField(null=True, related_name='+', to='ysgxuyu.Omtmse')),
            ],
        ),
        migrations.RemoveField(
            model_name='knoeepjnhs',
            name='azutzivj',
        ),
        migrations.RemoveField(
            model_name='knoeepjnhs',
            name='kluyzayvh',
        ),
        migrations.DeleteModel(
            name='Knoeepjnhs',
        ),
    ]
