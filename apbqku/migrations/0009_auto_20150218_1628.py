# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wulegwfs', '0008_auto_20150218_1627'),
        ('ukxhbn', '0007_auto_20150218_1628'),
        ('apbqku', '0008_ztmubrfn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uonrvb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ablgbcaw', models.OneToOneField(null=True, related_name='+', to='ukxhbn.Ikuwr')),
            ],
        ),
        migrations.RemoveField(
            model_name='tjpxiu',
            name='egyzjckxd',
        ),
        migrations.AddField(
            model_name='tjpxiu',
            name='jauqad',
            field=models.OneToOneField(null=True, related_name='+', to='wulegwfs.Txgqxz'),
        ),
    ]
