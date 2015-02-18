# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adlorvp', '0014_kzrfnfxko_uhhdmtehjg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kzrfnfxko',
            name='conaco',
        ),
        migrations.DeleteModel(
            name='Kzrfnfxko',
        ),
    ]
