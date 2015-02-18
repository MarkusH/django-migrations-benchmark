# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ukxhbn', '0003_delete_xtmekz'),
        ('khwbgr', '0003_auto_20150218_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ywojvtbwa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evkjp', models.OneToOneField(null=True, related_name='+', to='ukxhbn.Ikuwr')),
            ],
        ),
        migrations.DeleteModel(
            name='Qsqcspjrgx',
        ),
    ]
