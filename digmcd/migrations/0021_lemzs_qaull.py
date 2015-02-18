# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zsskgviadw', '0009_ylpjiaq_oztnvztcg'),
        ('digmcd', '0020_remove_xmvhvzui_iwugg'),
    ]

    operations = [
        migrations.AddField(
            model_name='lemzs',
            name='qaull',
            field=models.OneToOneField(null=True, related_name='+', to='zsskgviadw.Ylpjiaq'),
        ),
    ]
