# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yiupu', '0006_khayviiua'),
        ('adlorvp', '0020_remove_ehcuyeglmi_yfcgjm'),
        ('ruvaymw', '0020_auto_20150218_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ofvsocf',
            name='dahouzw',
        ),
        migrations.RemoveField(
            model_name='yckccoccsv',
            name='bhxiqpohj',
        ),
        migrations.AddField(
            model_name='ofvsocf',
            name='xlxvm',
            field=models.ForeignKey(null=True, related_name='+', to='yiupu.Zzsheqzf'),
        ),
        migrations.AddField(
            model_name='yckccoccsv',
            name='dwnni',
            field=models.CharField(default='', max_length=87),
        ),
        migrations.AddField(
            model_name='ylhrvymeyk',
            name='qsxlpvu',
            field=models.OneToOneField(null=True, related_name='+', to='adlorvp.Kmygwyorsi'),
        ),
    ]
