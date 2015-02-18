# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrmdjc', '0008_remove_gxoqulk_dbvbik'),
        ('ysgxuyu', '0010_auto_20150218_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eppkc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hcsrkzjk', models.OneToOneField(null=True, related_name='+', to='rrmdjc.Ddzxkrvtfd')),
            ],
        ),
        migrations.AddField(
            model_name='bmovnbnmed',
            name='exferamsuc',
            field=models.IntegerField(default=0),
        ),
    ]
