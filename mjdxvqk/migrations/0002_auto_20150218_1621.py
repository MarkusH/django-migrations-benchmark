# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0001_initial'),
        ('wulegwfs', '0001_initial'),
        ('mjdxvqk', '0001_initial'),
        ('zxxavsovs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vmnilim',
            name='vkvsbd',
            field=models.OneToOneField(null=True, related_name='+', to='zhavbmq.Ulvookvun'),
        ),
        migrations.AddField(
            model_name='tmgvpztce',
            name='mvirtxvn',
            field=models.ForeignKey(null=True, related_name='+', to='zxxavsovs.Fiellmltob'),
        ),
        migrations.AddField(
            model_name='edugsywcj',
            name='piqojyx',
            field=models.ForeignKey(null=True, related_name='+', to='wulegwfs.Yxsnty'),
        ),
    ]
