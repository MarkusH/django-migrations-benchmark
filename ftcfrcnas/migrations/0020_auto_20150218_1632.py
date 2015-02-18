# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qclaxc', '0018_auto_20150218_1632'),
        ('ftcfrcnas', '0019_auto_20150218_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fmzwd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anrkionx', models.ForeignKey(null=True, related_name='+', to='qclaxc.Hlpgeaqix')),
            ],
        ),
        migrations.AddField(
            model_name='myohdht',
            name='nafqslyyk',
            field=models.CharField(default='', max_length=207),
        ),
    ]
