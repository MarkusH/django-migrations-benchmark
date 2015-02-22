# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yiupu', '0001_initial'),
        ('rwlfplwktj', '0001_initial'),
        ('geemkrwi', '0002_auto_20150218_1621'),
    ]

    run_before = [
        ('yiupu', '0002_delete_jpmwh'),
    ]

    operations = [
        migrations.CreateModel(
            name='Begquxerkm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hyfisaxclk', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Eezxvbbvmn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redlewthb', models.OneToOneField(null=True, related_name='+', to='geemkrwi.Xtwdqfv')),
            ],
        ),
        migrations.CreateModel(
            name='Jkjvvohe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nezwu', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Kpjlirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qjfqxbl', models.CharField(default='', max_length=211)),
            ],
        ),
        migrations.CreateModel(
            name='Ojshxdt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fakazhjh', models.OneToOneField(null=True, related_name='+', to='yiupu.Jpmwh')),
            ],
        ),
        migrations.CreateModel(
            name='Qimzrcecmn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oqqkkpeiyp', models.CharField(default='', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Qqpfvbjbpk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciomneaa', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rsaiyadejv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yhkfpy', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Xqjugixefj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xvbpvsvwrw', models.OneToOneField(null=True, related_name='+', to='rwlfplwktj.Knoeepjnhs')),
            ],
        ),
    ]
