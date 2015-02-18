# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavygg', '0014_remove_jydvnf_xwilqwztoj'),
        ('mjdxvqk', '0015_auto_20150218_1628'),
        ('rqwywo', '0011_auto_20150218_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wmvmz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lincd', models.ForeignKey(null=True, related_name='+', to='zavygg.Gbmslrhm')),
            ],
        ),
        migrations.DeleteModel(
            name='Xaszfxobvf',
        ),
        migrations.RemoveField(
            model_name='huqprglqp',
            name='whhdjgrl',
        ),
        migrations.AddField(
            model_name='huqprglqp',
            name='atzdoio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='uxpep',
            name='uxbuqfdn',
            field=models.OneToOneField(null=True, related_name='+', to='mjdxvqk.Ovbcnxcwyr'),
        ),
    ]
