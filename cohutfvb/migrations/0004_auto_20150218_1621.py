# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joavhqi', '0002_auto_20150218_1621'),
        ('cohutfvb', '0003_crzqih'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livljpedso',
            name='xfxzoezgv',
        ),
        migrations.AddField(
            model_name='crzqih',
            name='uanao',
            field=models.OneToOneField(null=True, related_name='+', to='joavhqi.Lfssmpr'),
        ),
        migrations.AddField(
            model_name='livljpedso',
            name='ceudc',
            field=models.IntegerField(default=0),
        ),
    ]
