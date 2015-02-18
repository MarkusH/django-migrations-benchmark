# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zsskgviadw', '0006_auto_20150218_1627'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hcetattb',
        ),
        migrations.RemoveField(
            model_name='ltlsozji',
            name='djyxf',
        ),
        migrations.AddField(
            model_name='ltlsozji',
            name='dxeigdb',
            field=models.IntegerField(default=0),
        ),
    ]
