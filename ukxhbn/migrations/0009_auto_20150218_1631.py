# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digmcd', '0019_auto_20150218_1631'),
        ('ukxhbn', '0008_auto_20150218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aciaff',
            name='xjwwdbi',
        ),
        migrations.RemoveField(
            model_name='xqerjvxatp',
            name='kjyjccxd',
        ),
        migrations.AddField(
            model_name='aciaff',
            name='atqvcg',
            field=models.OneToOneField(null=True, related_name='+', to='digmcd.Zaganduq'),
        ),
        migrations.AddField(
            model_name='xqerjvxatp',
            name='vmulbes',
            field=models.IntegerField(default=0),
        ),
    ]
