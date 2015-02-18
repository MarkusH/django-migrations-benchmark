# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0016_delete_qrwsj'),
        ('rwlfplwktj', '0008_auto_20150218_1631'),
        ('cohutfvb', '0015_auto_20150218_1631'),
        ('rqwywo', '0013_auto_20150218_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gkiwtx',
            name='viugmj',
        ),
        migrations.RemoveField(
            model_name='jsvynw',
            name='cznktgglif',
        ),
        migrations.RemoveField(
            model_name='uxpep',
            name='uxbuqfdn',
        ),
        migrations.AddField(
            model_name='gkiwtx',
            name='pwsnbpros',
            field=models.OneToOneField(null=True, related_name='+', to='cohutfvb.Crzqih'),
        ),
        migrations.AddField(
            model_name='jsvynw',
            name='ommyuemmir',
            field=models.OneToOneField(null=True, related_name='+', to='rwlfplwktj.Yjzzdopc'),
        ),
        migrations.AddField(
            model_name='uxpep',
            name='jjioaflyak',
            field=models.OneToOneField(null=True, related_name='+', to='foijx.Flwuyjdlel'),
        ),
    ]
