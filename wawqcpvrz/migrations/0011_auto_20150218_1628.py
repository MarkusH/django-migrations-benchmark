# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adlorvp', '0016_auto_20150218_1628'),
        ('wawqcpvrz', '0010_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tyhxj',
            name='afzkaucmga',
        ),
        migrations.AddField(
            model_name='tyhxj',
            name='fzego',
            field=models.ForeignKey(null=True, related_name='+', to='adlorvp.Bauxko'),
        ),
    ]
