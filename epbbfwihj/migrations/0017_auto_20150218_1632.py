# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kfapsax', '0011_mygda'),
        ('epbbfwihj', '0016_dfjxgqll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Esslxuzogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gfvxxvbo', models.ForeignKey(null=True, related_name='+', to='kfapsax.Fxnrayf')),
            ],
        ),
        migrations.RemoveField(
            model_name='dfjxgqll',
            name='woifc',
        ),
        migrations.AddField(
            model_name='dfjxgqll',
            name='fqjpso',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='uwaayy',
            name='hmftxhnfr',
            field=models.IntegerField(default=0),
        ),
    ]
