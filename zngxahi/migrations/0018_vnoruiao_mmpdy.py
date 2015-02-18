# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wawqcpvrz', '0012_auto_20150218_1630'),
        ('zngxahi', '0017_auto_20150218_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='vnoruiao',
            name='mmpdy',
            field=models.ForeignKey(null=True, related_name='+', to='wawqcpvrz.Nqohhreonm'),
        ),
    ]
