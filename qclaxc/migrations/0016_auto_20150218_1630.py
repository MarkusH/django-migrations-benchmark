# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avwpufexob', '0014_auto_20150218_1630'),
        ('qclaxc', '0015_auto_20150218_1628'),
    ]

    run_before = [
        ('ysgxuyu', '0012_delete_bmovnbnmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yiifw',
            name='ufrqn',
        ),
        migrations.RemoveField(
            model_name='ilngaq',
            name='rhjodfszjd',
        ),
        migrations.RemoveField(
            model_name='ooecads',
            name='azjnmckmok',
        ),
        migrations.AddField(
            model_name='ilngaq',
            name='arwhqp',
            field=models.ForeignKey(null=True, related_name='+', to='avwpufexob.Yejdqycpmg'),
        ),
        migrations.AddField(
            model_name='ooecads',
            name='kjhiytbp',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Yiifw',
        ),
    ]
