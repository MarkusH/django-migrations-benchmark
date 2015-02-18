# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wulegwfs', '0009_auto_20150218_1628'),
        ('ysgxuyu', '0012_delete_bmovnbnmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='omtmse',
            name='ozlgxphz',
        ),
        migrations.RemoveField(
            model_name='eppkc',
            name='hcsrkzjk',
        ),
        migrations.AddField(
            model_name='eppkc',
            name='fdjqgbumm',
            field=models.ForeignKey(null=True, related_name='+', to='wulegwfs.Txgqxz'),
        ),
        migrations.DeleteModel(
            name='Omtmse',
        ),
    ]
