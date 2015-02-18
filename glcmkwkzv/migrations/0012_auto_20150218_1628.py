# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joavhqi', '0012_auto_20150218_1626'),
        ('glcmkwkzv', '0011_auto_20150218_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vkgguay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lnfahjzeib', models.ForeignKey(null=True, related_name='+', to='joavhqi.Yusanbjmh')),
            ],
        ),
        migrations.DeleteModel(
            name='Idmamodyjp',
        ),
    ]
