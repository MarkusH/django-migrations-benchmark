# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyxbcga', '0003_auto_20150218_1621'),
        ('irmtbds', '0003_rqzheruyb_dzqlaunuix'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rqzheruyb',
        ),
        migrations.RemoveField(
            model_name='bemqls',
            name='kiknreazyv',
        ),
        migrations.AddField(
            model_name='bemqls',
            name='aedocfocsn',
            field=models.ForeignKey(null=True, related_name='+', to='wyxbcga.Kpjlirt'),
        ),
    ]
