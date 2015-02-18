# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gbsaqmaxu', '0014_auto_20150218_1627'),
        ('irmtbds', '0007_remove_rqikftw_sjnjki'),
    ]

    operations = [
        migrations.CreateModel(
            name='Islmbaqxc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yqxhdtazhk', models.ForeignKey(null=True, related_name='+', to='gbsaqmaxu.Rkmtigdh')),
            ],
        ),
        migrations.RemoveField(
            model_name='bemqls',
            name='bjknddubg',
        ),
        migrations.AddField(
            model_name='bemqls',
            name='hqyqlzp',
            field=models.IntegerField(default=0),
        ),
    ]
