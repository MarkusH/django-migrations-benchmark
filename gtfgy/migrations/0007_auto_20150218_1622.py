# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emncdxt', '0004_auto_20150218_1621'),
        ('wawqcpvrz', '0003_scfuekgkl_rhgqd'),
        ('khwbgr', '0004_auto_20150218_1621'),
        ('gtfgy', '0006_auto_20150218_1621'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rgtvykx',
        ),
        migrations.RemoveField(
            model_name='ftwph',
            name='gatahehq',
        ),
        migrations.RemoveField(
            model_name='lbhtyfzldr',
            name='incygnnlw',
        ),
        migrations.RemoveField(
            model_name='swasd',
            name='jdzruuqtj',
        ),
        migrations.RemoveField(
            model_name='yrekcfrkl',
            name='ndgrspso',
        ),
        migrations.AddField(
            model_name='ftwph',
            name='gulgng',
            field=models.OneToOneField(null=True, related_name='+', to='emncdxt.Ktiod'),
        ),
        migrations.AddField(
            model_name='lbhtyfzldr',
            name='oqurkjppqv',
            field=models.ForeignKey(null=True, related_name='+', to='wawqcpvrz.Xivomw'),
        ),
        migrations.AddField(
            model_name='swasd',
            name='nhwmob',
            field=models.CharField(default='', max_length=52),
        ),
        migrations.AddField(
            model_name='yrekcfrkl',
            name='vgwig',
            field=models.ForeignKey(null=True, related_name='+', to='khwbgr.Ywojvtbwa'),
        ),
    ]
