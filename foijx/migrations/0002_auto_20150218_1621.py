# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0001_initial'),
        ('wulegwfs', '0001_initial'),
        ('ladqux', '0001_initial'),
        ('cohutfvb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wrafoshzom',
            name='gzayhaq',
            field=models.ForeignKey(null=True, related_name='+', to='ladqux.Oeyhu'),
        ),
        migrations.AddField(
            model_name='qqktwujdfq',
            name='uvyuhhx',
            field=models.OneToOneField(null=True, related_name='+', to='wulegwfs.Txgqxz'),
        ),
        migrations.AddField(
            model_name='flwuyjdlel',
            name='vvuquay',
            field=models.OneToOneField(null=True, related_name='+', to='wulegwfs.Txgqxz'),
        ),
        migrations.AddField(
            model_name='cnkdojs',
            name='adedvcyxhq',
            field=models.ForeignKey(null=True, related_name='+', to='cohutfvb.Sonmvoj'),
        ),
    ]
