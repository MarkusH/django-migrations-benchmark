# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavygg', '0015_auto_20150218_1630'),
        ('gtfgy', '0018_lbhtyfzldr_bqpchgui'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ohftljcts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wokzt', models.OneToOneField(null=True, related_name='+', to='zavygg.Jydvnf')),
            ],
        ),
        migrations.AddField(
            model_name='fnrijid',
            name='aifqvhai',
            field=models.IntegerField(default=0),
        ),
    ]
