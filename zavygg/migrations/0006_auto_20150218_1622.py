# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yiupu', '0003_auto_20150218_1621'),
        ('zavygg', '0005_auto_20150218_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gbmslrhm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wftcam', models.ForeignKey(null=True, related_name='+', to='yiupu.Zzsheqzf')),
            ],
        ),
        migrations.AddField(
            model_name='nzfoyhj',
            name='hqdxyajbhz',
            field=models.IntegerField(default=0),
        ),
    ]
