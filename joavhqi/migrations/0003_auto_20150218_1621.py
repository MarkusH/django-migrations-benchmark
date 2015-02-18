# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavygg', '0003_auto_20150218_1621'),
        ('qclaxc', '0003_auto_20150218_1621'),
        ('joavhqi', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rdhhdq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ztnjkzyby', models.OneToOneField(null=True, related_name='+', to='zavygg.Oqyncxevyj')),
            ],
        ),
        migrations.RemoveField(
            model_name='lfssmpr',
            name='udrjcs',
        ),
        migrations.AddField(
            model_name='lfssmpr',
            name='ulnuig',
            field=models.ForeignKey(null=True, related_name='+', to='qclaxc.Uajrm'),
        ),
    ]
