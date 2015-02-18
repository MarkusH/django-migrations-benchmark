# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zngxahi', '0002_auto_20150218_1621'),
        ('zsskgviadw', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ltlsozji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fzlko', models.ForeignKey(null=True, related_name='+', to='zngxahi.Kbgdzldxz')),
            ],
        ),
        migrations.RemoveField(
            model_name='hcetattb',
            name='njfdgh',
        ),
        migrations.AddField(
            model_name='hcetattb',
            name='dhmzbwvcg',
            field=models.CharField(default='', max_length=152),
        ),
    ]
