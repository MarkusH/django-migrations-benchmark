# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ysgxuyu', '0012_delete_bmovnbnmed'),
        ('adlorvp', '0016_auto_20150218_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ehcuyeglmi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yfcgjm', models.OneToOneField(null=True, related_name='+', to='ysgxuyu.Eppkc')),
            ],
        ),
        migrations.RemoveField(
            model_name='frzvg',
            name='jlbhm',
        ),
        migrations.DeleteModel(
            name='Frzvg',
        ),
    ]
