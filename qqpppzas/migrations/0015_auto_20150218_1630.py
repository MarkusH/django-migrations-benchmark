# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohutfvb', '0014_auto_20150218_1630'),
        ('qqpppzas', '0014_auto_20150218_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uxswpekqlt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('febtep', models.OneToOneField(null=True, related_name='+', to='cohutfvb.Ecgjvad')),
            ],
        ),
        migrations.RemoveField(
            model_name='shtlozkm',
            name='wjznogs',
        ),
        migrations.RemoveField(
            model_name='vdscpy',
            name='efspwnch',
        ),
        migrations.AddField(
            model_name='vdscpy',
            name='tcyjunatyh',
            field=models.CharField(default='', max_length=163),
        ),
    ]
