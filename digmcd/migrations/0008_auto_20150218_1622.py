# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glcmkwkzv', '0005_hbsqbahnce'),
        ('cmsrp', '0001_initial'),
        ('digmcd', '0007_auto_20150218_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lemzs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jaozjpsixx', models.OneToOneField(null=True, related_name='+', to='cmsrp.Ncysy')),
            ],
        ),
        migrations.RemoveField(
            model_name='untgafvod',
            name='pxzortn',
        ),
        migrations.RemoveField(
            model_name='zaganduq',
            name='kmmmtnspx',
        ),
        migrations.AddField(
            model_name='zaganduq',
            name='lxkoptjj',
            field=models.ForeignKey(null=True, related_name='+', to='glcmkwkzv.Unnork'),
        ),
    ]
