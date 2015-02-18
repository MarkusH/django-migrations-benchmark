# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foijx', '0006_auto_20150218_1622'),
        ('zngxahi', '0005_auto_20150218_1622'),
        ('cohutfvb', '0006_jrgrccoxvv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jrgrccoxvv',
            name='cgycqiur',
        ),
        migrations.AddField(
            model_name='crzqih',
            name='nenil',
            field=models.ForeignKey(null=True, related_name='+', to='foijx.Qqktwujdfq'),
        ),
        migrations.AddField(
            model_name='jrgrccoxvv',
            name='gjcirtejy',
            field=models.ForeignKey(null=True, related_name='+', to='zngxahi.Hiqedajgiu'),
        ),
    ]
