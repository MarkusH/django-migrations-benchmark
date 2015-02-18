# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruvaymw', '0012_auto_20150218_1625'),
        ('gbsaqmaxu', '0011_knqau_ytwbrbx'),
        ('burhjvc', '0012_remove_ydprem_wuxfyceg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ydprem',
            name='gjmyvkze',
        ),
        migrations.AddField(
            model_name='jnyynhgbb',
            name='iqfzdixyt',
            field=models.OneToOneField(null=True, related_name='+', to='ruvaymw.Faqagt'),
        ),
        migrations.AddField(
            model_name='ydprem',
            name='tazikiljv',
            field=models.ForeignKey(null=True, related_name='+', to='gbsaqmaxu.Nwyctrmqpq'),
        ),
    ]
