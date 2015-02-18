# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zsskgviadw', '0001_initial'),
        ('ukxhbn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gkiwtx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Huqprglqp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xumeqhx', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Lxcurbmhu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oncyszdy', models.CharField(default='', max_length=183)),
            ],
        ),
        migrations.CreateModel(
            name='Uxpep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wognfx', models.ForeignKey(null=True, related_name='+', to='zsskgviadw.Inyvz')),
            ],
        ),
        migrations.CreateModel(
            name='Xaszfxobvf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iskdepqo', models.OneToOneField(null=True, related_name='+', to='ukxhbn.Xtmekz')),
            ],
        ),
        migrations.AddField(
            model_name='gkiwtx',
            name='ouofvgrgp',
            field=models.ForeignKey(null=True, related_name='+', to='rqwywo.Lxcurbmhu'),
        ),
    ]
