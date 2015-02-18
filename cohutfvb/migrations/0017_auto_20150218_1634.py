# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glcmkwkzv', '0015_auto_20150218_1631'),
        ('cohutfvb', '0016_auto_20150218_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ckree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yqfsn', models.OneToOneField(null=True, related_name='+', to='glcmkwkzv.Fbytmhf')),
            ],
        ),
        migrations.RemoveField(
            model_name='ecgjvad',
            name='xoyasniyf',
        ),
        migrations.AddField(
            model_name='ecgjvad',
            name='mkqcu',
            field=models.IntegerField(default=0),
        ),
    ]
