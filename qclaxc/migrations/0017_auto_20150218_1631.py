# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wulegwfs', '0009_auto_20150218_1628'),
        ('uivaguf', '0016_auto_20150218_1628'),
        ('bniworfy', '0016_auto_20150218_1631'),
        ('qclaxc', '0016_auto_20150218_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Riwryjw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qfmyjzj', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='ggafntnbq',
            name='pqukuovutp',
        ),
        migrations.RemoveField(
            model_name='yswziiulyl',
            name='mzpaepi',
        ),
        migrations.AddField(
            model_name='ggafntnbq',
            name='jdpsqeljc',
            field=models.OneToOneField(null=True, related_name='+', to='wulegwfs.Wseerbko'),
        ),
        migrations.AddField(
            model_name='ooecads',
            name='wbopjvbl',
            field=models.OneToOneField(null=True, related_name='+', to='bniworfy.Trjyk'),
        ),
        migrations.AddField(
            model_name='yswziiulyl',
            name='omsizc',
            field=models.OneToOneField(null=True, related_name='+', to='uivaguf.Onmti'),
        ),
    ]
