# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuspknbh', '0017_auto_20150218_1632'),
        ('zsskgviadw', '0009_ylpjiaq_oztnvztcg'),
        ('rrmdjc', '0009_remove_guhhjm_ehzyfcfm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skeciabygt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blyex', models.ForeignKey(null=True, related_name='+', to='cuspknbh.Mwigq')),
            ],
        ),
        migrations.RemoveField(
            model_name='ddzxkrvtfd',
            name='vlpnxn',
        ),
        migrations.AddField(
            model_name='guhhjm',
            name='kgvpwpy',
            field=models.OneToOneField(null=True, related_name='+', to='zsskgviadw.Ylpjiaq'),
        ),
        migrations.DeleteModel(
            name='Ddzxkrvtfd',
        ),
    ]
