# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhavbmq', '0001_initial'),
        ('digmcd', '0002_xovte_fhgkhncfld'),
        ('zxxavsovs', '0001_initial'),
        ('rwlfplwktj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='untgafvod',
            name='pxzortn',
            field=models.ForeignKey(null=True, related_name='+', to='rwlfplwktj.Knoeepjnhs'),
        ),
        migrations.AddField(
            model_name='rdfrrg',
            name='yayujeww',
            field=models.ForeignKey(null=True, related_name='+', to='digmcd.Gxovs'),
        ),
        migrations.AddField(
            model_name='gtekbplhr',
            name='pdxvfhs',
            field=models.OneToOneField(null=True, related_name='+', to='zhavbmq.Vzhhl'),
        ),
        migrations.AddField(
            model_name='arqcdv',
            name='cffdghbzam',
            field=models.ForeignKey(null=True, related_name='+', to='zxxavsovs.Fiellmltob'),
        ),
    ]
