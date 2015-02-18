# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apbqku', '0007_delete_ffussl'),
        ('zxxavsovs', '0008_auto_20150218_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fiellmltob',
            name='xpmob',
        ),
        migrations.AddField(
            model_name='fiellmltob',
            name='cgcyzsjw',
            field=models.OneToOneField(null=True, related_name='+', to='apbqku.Tjpxiu'),
        ),
    ]
