# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uivaguf', '0007_auto_20150218_1623'),
        ('zavygg', '0007_auto_20150218_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edynlg',
            name='ghfqson',
        ),
        migrations.RemoveField(
            model_name='ligxr',
            name='rgamodph',
        ),
        migrations.AddField(
            model_name='ligxr',
            name='kfznkinf',
            field=models.OneToOneField(null=True, related_name='+', to='uivaguf.Ubuhm'),
        ),
    ]
