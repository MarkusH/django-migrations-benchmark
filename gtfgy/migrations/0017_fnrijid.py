# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joavhqi', '0013_auto_20150218_1628'),
        ('gtfgy', '0016_auto_20150218_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fnrijid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elgmg', models.OneToOneField(null=True, related_name='+', to='joavhqi.Lfssmpr')),
            ],
        ),
    ]
