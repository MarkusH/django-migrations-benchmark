# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zsskgviadw', '0002_auto_20150218_1621'),
        ('pkfudme', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heehdxfqyb',
            name='qoiuustxd',
        ),
        migrations.RemoveField(
            model_name='mnvmeraq',
            name='wskmkftbqi',
        ),
        migrations.AddField(
            model_name='heehdxfqyb',
            name='pimlfnkvip',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mnvmeraq',
            name='gutje',
            field=models.OneToOneField(null=True, related_name='+', to='zsskgviadw.Hcetattb'),
        ),
    ]
