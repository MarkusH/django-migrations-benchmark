# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsrp', '0003_ncysy_lkvgwwfoan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ncysy',
            name='lkvgwwfoan',
        ),
    ]
