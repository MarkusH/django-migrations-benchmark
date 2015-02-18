# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qclaxc', '0006_auto_20150218_1622'),
        ('zhavbmq', '0005_auto_20150218_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gwmyxcxdii',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lnioihvte', models.CharField(default='', max_length=33)),
            ],
        ),
        migrations.DeleteModel(
            name='Jznpks',
        ),
        migrations.RemoveField(
            model_name='bdniaupe',
            name='swdbw',
        ),
        migrations.AddField(
            model_name='dvkdj',
            name='jzwapass',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hmaopvcufb',
            name='xciop',
            field=models.ForeignKey(null=True, related_name='+', to='qclaxc.Yiifw'),
        ),
    ]
