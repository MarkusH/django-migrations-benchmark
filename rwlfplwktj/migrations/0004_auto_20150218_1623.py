# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rwlfplwktj', '0003_auto_20150218_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kgopo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xjvmy', models.CharField(default='', max_length=209)),
            ],
        ),
        migrations.RemoveField(
            model_name='xunyyu',
            name='haaxfgcmii',
        ),
        migrations.DeleteModel(
            name='Xunyyu',
        ),
    ]
