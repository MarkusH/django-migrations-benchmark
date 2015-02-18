# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ysgxuyu', '0008_auto_20150218_1626'),
        ('ladqux', '0006_auto_20150218_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iznpghp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sgafrav', models.OneToOneField(null=True, related_name='+', to='ysgxuyu.Bmovnbnmed')),
            ],
        ),
        migrations.AddField(
            model_name='oeyhu',
            name='pdbekl',
            field=models.IntegerField(default=0),
        ),
    ]
