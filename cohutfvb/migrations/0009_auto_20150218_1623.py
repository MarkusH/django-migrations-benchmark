# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digmcd', '0011_auto_20150218_1623'),
        ('cohutfvb', '0008_jrgrccoxvv_mimxt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jrgrccoxvv',
            name='gjcirtejy',
        ),
        migrations.AddField(
            model_name='qpuji',
            name='pozefnkorz',
            field=models.OneToOneField(null=True, related_name='+', to='digmcd.Gxovs'),
        ),
        migrations.DeleteModel(
            name='Jrgrccoxvv',
        ),
    ]
