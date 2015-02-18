# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakry', '0001_initial'),
        ('bniworfy', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='dkvkm',
            name='eylgo',
            field=models.OneToOneField(null=True, related_name='+', to='kakry.Aefqhqkmm'),
        ),
    ]
