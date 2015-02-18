# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrmdjc', '0005_gxoqulk_rlyebux'),
        ('zhavbmq', '0012_rywmfrbmil_hhpchb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rnddmd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ofhma', models.OneToOneField(null=True, related_name='+', to='rrmdjc.Ddzxkrvtfd')),
            ],
        ),
        migrations.RemoveField(
            model_name='rhhbgxx',
            name='owhkjq',
        ),
        migrations.DeleteModel(
            name='Rhhbgxx',
        ),
    ]
