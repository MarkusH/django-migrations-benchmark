# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnxyvqx', '0008_auto_20150218_1624'),
        ('cuspknbh', '0011_auto_20150218_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qotakup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mhctlvnto', models.ForeignKey(null=True, related_name='+', to='pnxyvqx.Nenfvguk')),
            ],
        ),
        migrations.DeleteModel(
            name='Yicalotegs',
        ),
        migrations.RemoveField(
            model_name='mwigq',
            name='shjxtfggcn',
        ),
        migrations.AddField(
            model_name='mwigq',
            name='aeynxtwrr',
            field=models.IntegerField(default=0),
        ),
    ]
