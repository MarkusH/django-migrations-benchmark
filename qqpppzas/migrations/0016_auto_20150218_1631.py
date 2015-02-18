# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kfapsax', '0011_mygda'),
        ('wyxbcga', '0015_delete_xqjugixefj'),
        ('qqpppzas', '0015_auto_20150218_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prljmjou',
            name='okelu',
        ),
        migrations.AddField(
            model_name='mukbde',
            name='hhunsf',
            field=models.OneToOneField(null=True, related_name='+', to='kfapsax.Fxnrayf'),
        ),
        migrations.AddField(
            model_name='prljmjou',
            name='wyhyzaku',
            field=models.ForeignKey(null=True, related_name='+', to='wyxbcga.Oblwdacdf'),
        ),
    ]
