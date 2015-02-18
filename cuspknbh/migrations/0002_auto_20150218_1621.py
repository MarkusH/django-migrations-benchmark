# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digmcd', '0001_initial'),
        ('cuspknbh', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='knkhh',
            name='vubojs',
            field=models.OneToOneField(null=True, related_name='+', to='digmcd.Untgafvod'),
        ),
        migrations.AddField(
            model_name='glbtwo',
            name='hdlrbpj',
            field=models.OneToOneField(null=True, related_name='+', to='digmcd.Gtekbplhr'),
        ),
    ]
