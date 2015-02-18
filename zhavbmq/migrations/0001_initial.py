# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnxyvqx', '0001_initial'),
        ('ladqux', '0001_initial'),
        ('apbqku', '0002_ssgsglh_yihuniyqgd'),
        ('cuspknbh', '0002_auto_20150218_1621'),
        ('avwpufexob', '0003_auto_20150218_1621'),
        ('epbbfwihj', '0002_auto_20150218_1621'),
        ('rqwywo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bdniaupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plgvgy', models.ForeignKey(null=True, related_name='+', to='apbqku.Ffussl')),
            ],
        ),
        migrations.CreateModel(
            name='Dvkdj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gsscvcgrm', models.OneToOneField(null=True, related_name='+', to='pnxyvqx.Nrnexasxp')),
            ],
        ),
        migrations.CreateModel(
            name='Hmaopvcufb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infpgx', models.ForeignKey(null=True, related_name='+', to='avwpufexob.Ubpmj')),
            ],
        ),
        migrations.CreateModel(
            name='Jznpks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lxipwqmi', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ohfvuo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gcobpdpoo', models.OneToOneField(null=True, related_name='+', to='epbbfwihj.Zfpgchkbaz')),
            ],
        ),
        migrations.CreateModel(
            name='Rhhbgxx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owhkjq', models.ForeignKey(null=True, related_name='+', to='ladqux.Zhgafcksok')),
            ],
        ),
        migrations.CreateModel(
            name='Ulvookvun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tugjdleqdq', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vzhhl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lucjyqsas', models.CharField(default='', max_length=69)),
            ],
        ),
        migrations.CreateModel(
            name='Ybkewg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuiqe', models.OneToOneField(null=True, related_name='+', to='rqwywo.Xaszfxobvf')),
            ],
        ),
        migrations.CreateModel(
            name='Yqtbfv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dvtoxrtyw', models.ForeignKey(null=True, related_name='+', to='cuspknbh.Ufrkff')),
            ],
        ),
    ]
