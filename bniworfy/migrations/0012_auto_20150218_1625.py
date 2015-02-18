# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuspknbh', '0011_auto_20150218_1625'),
        ('pkfudme', '0009_auto_20150218_1625'),
        ('bniworfy', '0011_auto_20150218_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vnjcuelh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yxlpab', models.ForeignKey(null=True, related_name='+', to='pkfudme.Ewxxluebq')),
            ],
        ),
        migrations.AddField(
            model_name='hqjqgiq',
            name='azbiiaoi',
            field=models.ForeignKey(null=True, related_name='+', to='cuspknbh.Mwigq'),
        ),
    ]
