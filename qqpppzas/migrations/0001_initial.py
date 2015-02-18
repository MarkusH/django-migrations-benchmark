# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kfapsax', '0001_initial'),
        ('zxxavsovs', '0001_initial'),
        ('yiupu', '0001_initial'),
        ('wulegwfs', '0001_initial'),
        ('glcmkwkzv', '0001_initial'),
        ('rqwywo', '0001_initial'),
        ('geemkrwi', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fzhxya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mvaeauil', models.OneToOneField(null=True, related_name='+', to='zxxavsovs.Fiellmltob')),
            ],
        ),
        migrations.CreateModel(
            name='Igtbspg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsqhvnp', models.OneToOneField(null=True, related_name='+', to='glcmkwkzv.Iwzqe')),
            ],
        ),
        migrations.CreateModel(
            name='Jchddfi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uteyef', models.ForeignKey(null=True, related_name='+', to='geemkrwi.Egvtran')),
            ],
        ),
        migrations.CreateModel(
            name='Lrqwbz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gqbcodrudr', models.OneToOneField(null=True, related_name='+', to='kfapsax.Sehvi')),
            ],
        ),
        migrations.CreateModel(
            name='Mukbde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laticxbs', models.OneToOneField(null=True, related_name='+', to='yiupu.Fzmiecxuo')),
            ],
        ),
        migrations.CreateModel(
            name='Prljmjou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('okelu', models.OneToOneField(null=True, related_name='+', to='wulegwfs.Txgqxz')),
            ],
        ),
        migrations.CreateModel(
            name='Shtlozkm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zwsomb', models.ForeignKey(null=True, related_name='+', to='wulegwfs.Txgqxz')),
            ],
        ),
        migrations.CreateModel(
            name='Vdscpy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('efspwnch', models.OneToOneField(null=True, related_name='+', to='rqwywo.Huqprglqp')),
            ],
        ),
        migrations.CreateModel(
            name='Xcuutwsyfn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bwpigha', models.CharField(default='', max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Ybcxw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mwpkhqrbva', models.CharField(default='', max_length=218)),
            ],
        ),
    ]
