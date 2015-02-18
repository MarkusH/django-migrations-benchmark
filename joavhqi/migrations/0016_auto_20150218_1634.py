# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uivaguf', '0018_auto_20150218_1634'),
        ('joavhqi', '0015_auto_20150218_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uodtjnez',
            name='qacrcmfud',
        ),
        migrations.RemoveField(
            model_name='lfssmpr',
            name='rxrepc',
        ),
        migrations.RemoveField(
            model_name='oyjnlgzy',
            name='qmfhtty',
        ),
        migrations.AddField(
            model_name='lfssmpr',
            name='kighcjrg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='oyjnlgzy',
            name='jgdrzj',
            field=models.ForeignKey(null=True, related_name='+', to='uivaguf.Zwjgfcdi'),
        ),
        migrations.DeleteModel(
            name='Uodtjnez',
        ),
    ]
