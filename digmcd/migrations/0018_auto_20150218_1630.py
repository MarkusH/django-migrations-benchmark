# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emncdxt', '0012_shgjep_qucvdgncbq'),
        ('digmcd', '0017_auto_20150218_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rozpduya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hhmhbd', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='yymzlvsz',
            name='qwacibmrk',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='zaganduq',
            name='bxgqiay',
            field=models.OneToOneField(null=True, related_name='+', to='emncdxt.Gnxmv'),
        ),
        migrations.AddField(
            model_name='zyjgcrtsvt',
            name='eqpvez',
            field=models.CharField(default='', max_length=188),
        ),
    ]
