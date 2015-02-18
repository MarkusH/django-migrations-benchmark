# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adlorvp', '0012_remove_afyxxcmzds_nfvueppp'),
        ('zavygg', '0010_delete_twdtvqs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Nzfoyhj',
        ),
        migrations.RemoveField(
            model_name='hitvmegxki',
            name='qufssktrdx',
        ),
        migrations.RemoveField(
            model_name='kihvqrmtr',
            name='zvauzxvz',
        ),
        migrations.AddField(
            model_name='hitvmegxki',
            name='xyxla',
            field=models.CharField(default='', max_length=211),
        ),
        migrations.AddField(
            model_name='kihvqrmtr',
            name='lxnjosrj',
            field=models.OneToOneField(null=True, related_name='+', to='adlorvp.Phrzexgxu'),
        ),
    ]
