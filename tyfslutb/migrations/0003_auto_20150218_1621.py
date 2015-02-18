# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wawqcpvrz', '0002_delete_vrvslusmy'),
        ('tyfslutb', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ckvpx',
            name='dtnnovz',
        ),
        migrations.RemoveField(
            model_name='juemb',
            name='objhsjj',
        ),
        migrations.RemoveField(
            model_name='qhzppcqwku',
            name='xjbinng',
        ),
        migrations.AddField(
            model_name='ckvpx',
            name='jjgracphi',
            field=models.CharField(default='', max_length=112),
        ),
        migrations.AddField(
            model_name='qhzppcqwku',
            name='nzmchjwxlf',
            field=models.CharField(default='', max_length=38),
        ),
        migrations.AddField(
            model_name='ynbpgqn',
            name='dpwwwnuj',
            field=models.OneToOneField(null=True, related_name='+', to='wawqcpvrz.Nrmckl'),
        ),
    ]
