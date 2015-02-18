# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avwpufexob', '0005_auto_20150218_1621'),
        ('ysgxuyu', '0002_kqlunbkaa_cexmjva'),
    ]

    operations = [
        migrations.CreateModel(
            name='Njigbqwuqa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdfqlfnegc', models.ForeignKey(null=True, related_name='+', to='avwpufexob.Nhpkrhkql')),
            ],
        ),
        migrations.RemoveField(
            model_name='kqlunbkaa',
            name='cexmjva',
        ),
    ]
