# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0007_auto_20150218_1622'),
        ('geemkrwi', '0006_wilsmoea_ninajhwzfe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='egvtran',
            name='mhnvmmxnvf',
        ),
        migrations.AddField(
            model_name='egvtran',
            name='iaywdnrfj',
            field=models.OneToOneField(null=True, related_name='+', to='foijx.Wrafoshzom'),
        ),
    ]
