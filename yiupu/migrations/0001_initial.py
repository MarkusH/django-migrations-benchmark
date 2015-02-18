# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygnakzgjxu', '0001_initial'),
        ('mntrwrm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fzmiecxuo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wpvqrrkg', models.OneToOneField(null=True, related_name='+', to='ygnakzgjxu.Mxlpodxpm')),
            ],
        ),
        migrations.CreateModel(
            name='Jpmwh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jftgansub', models.CharField(default='', max_length=253)),
            ],
        ),
        migrations.CreateModel(
            name='Zzsheqzf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdlqispdp', models.ForeignKey(null=True, related_name='+', to='mntrwrm.Xzicjkogl')),
            ],
        ),
    ]
