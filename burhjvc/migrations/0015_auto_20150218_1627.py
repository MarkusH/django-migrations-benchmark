# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burhjvc', '0014_remove_qwtnucajp_efhmvghs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ydprem',
            name='tazikiljv',
        ),
        migrations.AddField(
            model_name='qbuqivoko',
            name='vupdohnyr',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Ydprem',
        ),
    ]
