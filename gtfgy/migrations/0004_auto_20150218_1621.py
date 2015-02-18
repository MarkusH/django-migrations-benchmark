# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emncdxt', '0004_auto_20150218_1621'),
        ('ysgxuyu', '0001_initial'),
        ('gtfgy', '0003_niwaoqfft_serhcyqy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yrekcfrkl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ndgrspso', models.CharField(default='', max_length=49)),
            ],
        ),
        migrations.RemoveField(
            model_name='xqcngusl',
            name='vgeuicxo',
        ),
        migrations.RemoveField(
            model_name='rykamine',
            name='ofjjiorcjg',
        ),
        migrations.RemoveField(
            model_name='swasd',
            name='xlzvsww',
        ),
        migrations.AddField(
            model_name='rykamine',
            name='gwpcavl',
            field=models.OneToOneField(null=True, related_name='+', to='emncdxt.Ktiod'),
        ),
        migrations.AddField(
            model_name='swasd',
            name='jdzruuqtj',
            field=models.ForeignKey(null=True, related_name='+', to='ysgxuyu.Bmovnbnmed'),
        ),
        migrations.DeleteModel(
            name='Xqcngusl',
        ),
    ]
