# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khwbgr', '0009_auto_20150218_1630'),
        ('zsskgviadw', '0008_auto_20150218_1630'),
        ('ruvaymw', '0018_auto_20150218_1630'),
    ]

    run_before = [
        ('foijx', '0016_delete_qrwsj'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frzjpchfpt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cqinuxmtx', models.OneToOneField(null=True, related_name='+', to='khwbgr.Ibuazau')),
            ],
        ),
        migrations.RemoveField(
            model_name='zpubci',
            name='mvnkwqm',
        ),
        migrations.AddField(
            model_name='bdpibttuxi',
            name='sydxidrt',
            field=models.CharField(default='', max_length=205),
        ),
        migrations.AddField(
            model_name='swanlanqxn',
            name='skdyouf',
            field=models.ForeignKey(null=True, related_name='+', to='zsskgviadw.Ltlsozji'),
        ),
    ]
