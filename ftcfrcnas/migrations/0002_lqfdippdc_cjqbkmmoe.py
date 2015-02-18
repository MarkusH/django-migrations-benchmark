# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcfrcnas', '0001_initial'),
        ('irmtbds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lqfdippdc',
            name='cjqbkmmoe',
            field=models.ForeignKey(null=True, related_name='+', to='irmtbds.Bemqls'),
        ),
    ]
