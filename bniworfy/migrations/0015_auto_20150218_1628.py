# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rwlfplwktj', '0007_yjzzdopc'),
        ('bniworfy', '0014_hqjqgiq_vcffvafyek'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dvqne',
            name='ubeuubhtm',
        ),
        migrations.AddField(
            model_name='dvqne',
            name='hgcwzkpp',
            field=models.OneToOneField(null=True, related_name='+', to='rwlfplwktj.Yjzzdopc'),
        ),
        migrations.AddField(
            model_name='gsmbfohda',
            name='ewlbpn',
            field=models.IntegerField(default=0),
        ),
    ]
