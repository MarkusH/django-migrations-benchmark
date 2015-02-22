# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apbqku', '0005_auto_20150218_1622'),
        ('ygnakzgjxu', '0005_xpmnn_moifgm'),
    ]

    run_before = [
        ('esznwrr', '0004_delete_vppjpa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ttzean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zosoxtv', models.ForeignKey(null=True, related_name='+', to='apbqku.Ffussl')),
            ],
        ),
        migrations.RemoveField(
            model_name='xpmnn',
            name='moifgm',
        ),
        migrations.DeleteModel(
            name='Xpmnn',
        ),
    ]
