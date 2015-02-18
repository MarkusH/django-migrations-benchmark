# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohutfvb', '0010_remove_qpuji_pozefnkorz'),
        ('cuspknbh', '0010_mbcah_auvyvqhx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mbcah',
            name='ddbfeooid',
        ),
        migrations.RemoveField(
            model_name='mwigq',
            name='uwtfws',
        ),
        migrations.AddField(
            model_name='mwigq',
            name='shjxtfggcn',
            field=models.OneToOneField(null=True, related_name='+', to='cohutfvb.Livljpedso'),
        ),
    ]
