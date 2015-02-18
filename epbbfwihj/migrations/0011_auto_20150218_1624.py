# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ladqux', '0005_auto_20150218_1624'),
        ('apbqku', '0005_auto_20150218_1622'),
        ('epbbfwihj', '0010_auto_20150218_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sysnlv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ybqvecvb', models.OneToOneField(null=True, related_name='+', to='apbqku.Tjpxiu')),
            ],
        ),
        migrations.RemoveField(
            model_name='uzdthbetj',
            name='qrawui',
        ),
        migrations.AddField(
            model_name='zfpgchkbaz',
            name='axmnlbmf',
            field=models.ForeignKey(null=True, related_name='+', to='ladqux.Yfyadqk'),
        ),
    ]
