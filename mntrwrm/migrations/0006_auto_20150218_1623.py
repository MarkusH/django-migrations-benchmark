# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mntrwrm', '0005_auto_20150218_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ysslx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('znehtaygp', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='eaeehqi',
            name='tauahpur',
            field=models.CharField(default='', max_length=14),
        ),
    ]
