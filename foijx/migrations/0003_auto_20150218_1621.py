# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnxyvqx', '0002_nrnexasxp_dzshhvc'),
        ('foijx', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mvmwqukrbx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ffobkibqn', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Nznejqg',
        ),
        migrations.AddField(
            model_name='qqktwujdfq',
            name='uecimvq',
            field=models.ForeignKey(null=True, related_name='+', to='pnxyvqx.Nrnexasxp'),
        ),
    ]
