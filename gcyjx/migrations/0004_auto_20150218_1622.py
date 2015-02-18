# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geemkrwi', '0006_wilsmoea_ninajhwzfe'),
        ('gcyjx', '0003_auto_20150218_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xdvbgtxz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yjlhhuvyi', models.OneToOneField(null=True, related_name='+', to='geemkrwi.Mxvmqmhku')),
            ],
        ),
        migrations.RemoveField(
            model_name='snjsz',
            name='uxkarnxudp',
        ),
        migrations.AddField(
            model_name='snjsz',
            name='vyrxggwcrm',
            field=models.CharField(default='', max_length=50),
        ),
    ]
