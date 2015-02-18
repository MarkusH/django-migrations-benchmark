# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yiupu', '0001_initial'),
        ('mntrwrm', '0001_initial'),
        ('adlorvp', '0002_kzrfnfxko_rfezjxndz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cdardz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wdjjcbyo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Iwhkq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Lqfdippdc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Myohdht',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lybemykxx', models.OneToOneField(null=True, related_name='+', to='mntrwrm.Rbhubw')),
            ],
        ),
        migrations.CreateModel(
            name='Ncptyh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kvfaskmmrq', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Qibygpddzw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hachwpnpia', models.ForeignKey(null=True, related_name='+', to='yiupu.Jpmwh')),
            ],
        ),
        migrations.CreateModel(
            name='Qrwqtj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssdfr', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Snszfzibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nfcbptbpxv', models.CharField(default='', max_length=21)),
            ],
        ),
        migrations.CreateModel(
            name='Sukkrqb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vsgwbct', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Wjxepwd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppndehjbmf', models.ForeignKey(null=True, related_name='+', to='adlorvp.Tpxhcuni')),
            ],
        ),
    ]
