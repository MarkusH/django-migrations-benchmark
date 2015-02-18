# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtfgy', '0017_fnrijid'),
        ('geemkrwi', '0014_auto_20150218_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='hxkigetost',
            name='gvsmh',
            field=models.OneToOneField(null=True, related_name='+', to='gtfgy.Fnrijid'),
        ),
    ]
