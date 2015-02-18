# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkfudme', '0007_auto_20150218_1623'),
        ('ruvaymw', '0010_remove_owamswc_owxxem'),
        ('geemkrwi', '0009_auto_20150218_1623'),
        ('joavhqi', '0007_remove_uodtjnez_rasnn'),
    ]

    operations = [
        migrations.AddField(
            model_name='iowgy',
            name='pihqhp',
            field=models.ForeignKey(null=True, related_name='+', to='pkfudme.Dbpile'),
        ),
        migrations.AddField(
            model_name='nizqeesp',
            name='qmhtlk',
            field=models.OneToOneField(null=True, related_name='+', to='ruvaymw.Bdpibttuxi'),
        ),
        migrations.AddField(
            model_name='uodtjnez',
            name='qacrcmfud',
            field=models.ForeignKey(null=True, related_name='+', to='geemkrwi.Mxvmqmhku'),
        ),
    ]
