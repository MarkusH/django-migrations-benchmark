# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyxbcga', '0016_remove_qqpfvbjbpk_ebcai'),
        ('cmsrp', '0008_auto_20150218_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bovkv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yzohilanvo', models.ForeignKey(null=True, related_name='+', to='wyxbcga.Begquxerkm')),
            ],
        ),
        migrations.RemoveField(
            model_name='vlmfay',
            name='fejusiz',
        ),
        migrations.DeleteModel(
            name='Vlmfay',
        ),
    ]
