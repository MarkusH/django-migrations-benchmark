# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burhjvc', '0002_auto_20150218_1621'),
        ('pkfudme', '0001_initial'),
        ('wulegwfs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bmovnbnmed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zczgojzvsb', models.OneToOneField(null=True, related_name='+', to='pkfudme.Mnvmeraq')),
            ],
        ),
        migrations.CreateModel(
            name='Kqlunbkaa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vccxl', models.OneToOneField(null=True, related_name='+', to='wulegwfs.Txgqxz')),
            ],
        ),
        migrations.CreateModel(
            name='Omtmse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipywv', models.ForeignKey(null=True, related_name='+', to='burhjvc.Pdzdhpq')),
            ],
        ),
    ]
