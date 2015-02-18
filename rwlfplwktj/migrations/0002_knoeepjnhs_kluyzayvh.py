# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rwlfplwktj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='knoeepjnhs',
            name='kluyzayvh',
            field=models.ForeignKey(null=True, related_name='+', to='rwlfplwktj.Knoeepjnhs'),
        ),
    ]
